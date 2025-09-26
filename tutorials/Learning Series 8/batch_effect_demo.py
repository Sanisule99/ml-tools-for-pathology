import numpy as np, pandas as pd, matplotlib.pyplot as plt, os, argparse, yaml
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import umap

def simulate(n=600, n_sites=4, n_classes=3, seed=42):
    rng = np.random.default_rng(seed)
    site = rng.integers(0, n_sites, size=n)
    y = rng.integers(0, n_classes, size=n)
    # true class signal
    mu_class = rng.normal(0, 2, size=(n_classes, 8))
    X = mu_class[y] + rng.normal(0, 1, size=(n, 8))
    # add site batch shift
    site_shift = rng.normal(0, 3, size=(n_sites, 8))
    X += site_shift[site]
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(8)])
    df["site"] = site; df["y"] = y
    return df

def combat_like(df, batch_col="site", feature_cols=None):
    # very lightweight "center per batch" correction (not full ComBat)
    if feature_cols is None:
        feature_cols = [c for c in df.columns if c.startswith("f")]
    X = df[feature_cols].copy()
    for b in df[batch_col].unique():
        idx = df[batch_col]==b
        X.loc[idx] = X.loc[idx] - X.loc[idx].mean(axis=0)
    out = df.copy()
    out[feature_cols] = X
    return out

def embedd(df, feature_cols, title, outpath):
    X = df[feature_cols].values
    Xs = StandardScaler().fit_transform(X)
    p = PCA(n_components=2).fit_transform(Xs)
    reducer = umap.UMAP(n_components=2, random_state=42)
    u = reducer.fit_transform(Xs)
    fig, axes = plt.subplots(1,2, figsize=(10,4))
    sc0 = axes[0].scatter(p[:,0], p[:,1], c=df["site"], s=12)
    axes[0].set_title(title+" — PCA (colored by site)")
    sc1 = axes[1].scatter(u[:,0], u[:,1], c=df["site"], s=12)
    axes[1].set_title(title+" — UMAP (colored by site)")
    for ax in axes: ax.set_xticks([]); ax.set_yticks([])
    plt.tight_layout(); plt.savefig(outpath); plt.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n_sites", type=int, default=None)
    ap.add_argument("--n_classes", type=int, default=None)
    ap.add_argument("--n", type=int, default=None)
    args = ap.parse_args()

    with open("config.yaml") as f: cfg = yaml.safe_load(f)
    n_sites = args.n_sites or cfg["N_SITES"]
    n_classes = args.n_classes or cfg["N_CLASSES"]
    n = args.n or cfg["N"]
    outdir = cfg["OUTPUT_DIR"]; os.makedirs(outdir, exist_ok=True)

    df = simulate(n=n, n_sites=n_sites, n_classes=n_classes)
    feats = [c for c in df.columns if c.startswith("f")]
    embedd(df, feats, "Before correction", os.path.join(outdir, "pca_umap_before.png"))
    df_corr = combat_like(df, "site", feats)
    embedd(df_corr, feats, "After per-site centering", os.path.join(outdir, "pca_umap_after.png"))
    print(f"Saved: {outdir}/pca_umap_before.png and pca_umap_after.png")
