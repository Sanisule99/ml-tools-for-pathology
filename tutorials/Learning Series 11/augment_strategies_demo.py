import argparse, os, random
import numpy as np
import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import yaml

def set_seed(s=42):
    random.seed(s); np.random.seed(s); torch.manual_seed(s)

def make_grid(imgs, out):
    cols = len(imgs)
    fig, axes = plt.subplots(1, cols, figsize=(2.5*cols, 2.5))
    if cols==1: axes=[axes]
    for ax, t in zip(axes, imgs):
        im = t.permute(1,2,0).numpy()
        im = np.clip(im, 0, 1)
        ax.imshow(im); ax.axis("off")
    plt.tight_layout(); plt.savefig(out); plt.close()

def mixup(a, b, alpha=0.4):
    lam = np.random.beta(alpha, alpha)
    return lam*a + (1-lam)*b

def cutmix(a, b):
    _, h, w = a.shape
    ch, cw = h//3, w//3
    y = np.random.randint(h - ch)
    x = np.random.randint(w - cw)
    out = a.clone()
    out[:, y:y+ch, x:x+cw] = b[:, y:y+ch, x:x+cw]
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data_dir", type=str, default="data/mini")
    ap.add_argument("--img_size", type=int, default=224)
    args = ap.parse_args()

    os.makedirs("outputs", exist_ok=True)
    tfm = transforms.Compose([transforms.Resize((args.img_size,args.img_size)), transforms.ToTensor()])
    ds = datasets.ImageFolder(args.data_dir, transform=tfm)
    if len(ds) < 4:
        print("Please add a few images under data/mini/<class>/*.png"); exit(0)

    set_seed(42)
    a,_ = ds[0]; b,_ = ds[1]; c,_ = ds[2]; d,_ = ds[3]
    make_grid([a, b, mixup(a,b), mixup(c,d)], "outputs/mixup_grid.png")
    make_grid([a, b, cutmix(a,b), cutmix(c,d)], "outputs/cutmix_grid.png")

    color = transforms.ColorJitter(brightness=0.25, contrast=0.25, saturation=0.2, hue=0.05)
    a2 = color(a); b2 = color(b); c2 = color(c); d2 = color(d)
    make_grid([a, a2, b, b2, c2], "outputs/colorjitter_grid.png")
    print("Saved grids to outputs/: mixup_grid.png, cutmix_grid.png, colorjitter_grid.png")
