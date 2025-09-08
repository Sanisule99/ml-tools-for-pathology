
from __future__ import annotations
import numpy as np, pandas as pd

def harmonize_barcode(x: str, level: str = "sample") -> str:
    if not isinstance(x, str): return x
    parts = x.split("-")
    if len(parts) < 3: return x
    return "-".join(parts[:3]) if level=="patient" else "-".join(parts[:4])

def make_clinical(clinical_raw: pd.DataFrame, id_col: str, time_col: str, event_col: str,
                  covariates: list[str] | None = None, barcode_level: str = "sample") -> pd.DataFrame:
    covariates = covariates or []
    df = clinical_raw.copy()
    df["sample_id"] = df[id_col].astype(str).map(lambda s: harmonize_barcode(s, barcode_level))
    out_cols = ["sample_id", time_col, event_col] + [c for c in covariates if c in df.columns]
    df = df[out_cols].rename(columns={time_col:"OS_time", event_col:"OS_event"})
    df["OS_event"] = df["OS_event"].astype(int)
    df = df.dropna(subset=["sample_id","OS_time","OS_event"]).drop_duplicates("sample_id")
    return df

def make_expression(expr_raw: pd.DataFrame, index_as: str, gene_col: str|None=None,
                    sample_cols: list[str] | None=None) -> pd.DataFrame:
    if index_as == "rows_are_genes":
        df = expr_raw.copy()
        if gene_col is None: gene_col = df.columns[0]
        df = df.set_index(gene_col).T
        df.insert(0, "sample_id", df.index)
        return df.reset_index(drop=True)
    elif index_as == "long":
        assert gene_col is not None and sample_cols is not None
        gene = gene_col; sid, val = sample_cols
        mat = expr_raw.pivot_table(index=sid, columns=gene, values=val, aggfunc="mean").reset_index().rename(columns={sid:"sample_id"})
        return mat
    else:
        raise ValueError("Unsupported index_as")

def make_maf(maf_raw: pd.DataFrame, sample_col="Tumor_Sample_Barcode", gene_col="Hugo_Symbol",
             class_col="Variant_Classification", keep_classes: list[str] | None=None, barcode_level="sample") -> pd.DataFrame:
    df = maf_raw.copy()
    df[sample_col] = df[sample_col].astype(str).map(lambda s: harmonize_barcode(s, barcode_level))
    rename = {sample_col:"Tumor_Sample_Barcode", gene_col:"Hugo_Symbol", class_col:"Variant_Classification"}
    df = df.rename(columns=rename)[["Tumor_Sample_Barcode","Hugo_Symbol","Variant_Classification"]]
    if keep_classes: df = df[df["Variant_Classification"].isin(keep_classes)]
    return df.dropna(subset=["Tumor_Sample_Barcode","Hugo_Symbol"])

def intersect_ids(clinical: pd.DataFrame, expr: pd.DataFrame, maf: pd.DataFrame):
    ids = set(clinical["sample_id"]).intersection(expr["sample_id"]).intersection(maf["Tumor_Sample_Barcode"])
    return (clinical[clinical["sample_id"].isin(ids)].copy(),
            expr[expr["sample_id"].isin(ids)].copy(),
            maf[maf["Tumor_Sample_Barcode"].isin(ids)].copy())

def make_driver_flags(maf: pd.DataFrame, drivers: list[str]) -> pd.DataFrame:
    m = (maf.assign(flag=1)
           .pivot_table(index="Tumor_Sample_Barcode", columns="Hugo_Symbol", values="flag", aggfunc="max", fill_value=0))
    m = m.reindex(columns=drivers, fill_value=0).reset_index().rename(columns={"Tumor_Sample_Barcode":"sample_id"})
    m.columns = ["sample_id"] + [f"{g}_mut" for g in drivers]
    return m

def mutation_burden(maf: pd.DataFrame) -> pd.DataFrame:
    mb = (maf.dropna(subset=["Hugo_Symbol"])
            .groupby("Tumor_Sample_Barcode")["Hugo_Symbol"].nunique()
            .rename("mut_burden").reset_index())
    return mb.rename(columns={"Tumor_Sample_Barcode":"sample_id"})
