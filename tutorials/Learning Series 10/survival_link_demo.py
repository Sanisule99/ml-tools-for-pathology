import numpy as np, pandas as pd, matplotlib.pyplot as plt, os
from lifelines import KaplanMeierFitter, CoxPHFitter
from sklearn.preprocessing import StandardScaler
import yaml

def simulate(n=400, seed=42):
    rng = np.random.default_rng(seed)
    grade = rng.normal(0,1,size=n)
    feat = rng.normal(0,1,size=n)
    # hazard increases with grade+feat
    baseline = rng.exponential(scale=10, size=n)
    risk = np.exp(0.6*grade + 0.4*feat)
    time = baseline / risk
    event = rng.binomial(1, 0.7, size=n)
    df = pd.DataFrame({"time": time, "event": event, "grade": grade, "feat": feat})
    # create high/low groups for KM
    df["feat_bin"] = (df["feat"] > df["feat"].median()).astype(int)
    return df

if __name__ == "__main__":
    with open("config.yaml","w") as f: f.write("OUTPUT_DIR: outputs\nSEED: 42\n")
    with open("config.yaml") as f: cfg = yaml.safe_load(f)
    os.makedirs(cfg["OUTPUT_DIR"], exist_ok=True)
    df = simulate(seed=cfg["SEED"])
    # KM plot
    km = KaplanMeierFitter()
    fig = plt.figure(figsize=(6,4))
    for grp, label in [(0, "Low feat"), (1, "High feat")]:
        mask = df["feat_bin"]==grp
        km.fit(df.loc[mask, "time"], df.loc[mask, "event"], label=label)
        km.plot_survival_function()
    plt.title("Kaplan–Meier by feature bin"); plt.tight_layout()
    plt.savefig(os.path.join(cfg["OUTPUT_DIR"], "km_curves.png")); plt.close()

    # Cox PH
    cph = CoxPHFitter()
    cph.fit(df[["time","event","grade","feat"]], duration_col="time", event_col="event")
    with open(os.path.join(cfg["OUTPUT_DIR"], "cox_summary.txt"), "w") as f:
        f.write(cph.summary.to_string())
    print("Saved km_curves.png and cox_summary.txt to outputs/")
