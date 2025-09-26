import torch, torch.nn as nn
import torch.nn.functional as F
from torchvision.transforms import ToTensor
import numpy as np, matplotlib.pyplot as plt, os

def make_shapes(n=400, img_size=64, seed=42):
    rng = np.random.default_rng(seed)
    X = np.zeros((n, 1, img_size, img_size), dtype=np.float32)
    y = np.zeros((n,), dtype=np.int64)
    for i in range(n):
        canvas = np.zeros((img_size, img_size), dtype=np.float32)
        cls = rng.integers(0,2) # 0 circle, 1 square
        y[i] = cls
        cx, cy = rng.integers(16, img_size-16, size=2)
        r = rng.integers(6, 12)
        if cls==0:
            yy, xx = np.ogrid[:img_size,:img_size]
            mask = (xx-cx)**2 + (yy-cy)**2 <= r**2
            canvas[mask] = 1.0
        else:
            canvas[cy-r:cy+r, cx-r:cx+r] = 1.0
        X[i,0] = canvas
    return torch.tensor(X), torch.tensor(y)

class TinyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(1, 8, 3, padding=1)
        self.fc = nn.Linear(8*32*32, 2)
    def forward(self, x):
        x = F.relu(self.conv(x))
        x = F.max_pool2d(x,2)
        x = x.view(x.size(0), -1)
        return self.fc(x)

def saliency(model, x, target):
    x = x.clone().detach().requires_grad_(True)
    out = model(x)
    loss = F.cross_entropy(out, target)
    loss.backward()
    return x.grad.abs().max(dim=1)[0].detach()

if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    X, y = make_shapes(n=400)
    train_x, test_x = X[:320], X[320:]
    train_y, test_y = y[:320], y[320:]
    model = TinyCNN()
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    for epoch in range(20):
        opt.zero_grad()
        out = model(train_x)
        loss = F.cross_entropy(out, train_y)
        loss.backward(); opt.step()
    idx = 5
    s = saliency(model, test_x[idx:idx+1], test_y[idx:idx+1])[0].numpy()
    img = test_x[idx,0].numpy()
    fig, axes = plt.subplots(1,2, figsize=(6,3))
    axes[0].imshow(img); axes[0].set_title("Input"); axes[0].axis("off")
    axes[1].imshow(s); axes[1].set_title("Saliency (abs grad)"); axes[1].axis("off")
    plt.tight_layout(); plt.savefig("outputs/saliency_demo.png")
    print("Saved outputs/saliency_demo.png")
