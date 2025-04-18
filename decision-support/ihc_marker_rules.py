def get_top_markers_for_tissue(tissue):
    """
    Return top tissue-specific IHC markers based on GTEx data.
    """
    tissue_map = {
        "Liver": ["ALB", "HP", "TF"],
        "Prostate": ["KLK3", "ACPP", "NKX3-1"],
        "Colon": ["CDX2", "CK20", "MUC2"],
        "Breast": ["GATA3", "ESR1", "KRT18"],
        "Lung": ["TTF1", "NAPSA", "SFTPB"]
    }
    return tissue_map.get(tissue, ["No marker data available for this tissue"])
