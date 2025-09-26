import argparse, os
import open_clip
import torch
from PIL import Image

def load_model():
    model, preprocess, _ = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
    tokenizer = open_clip.get_tokenizer('ViT-B-32')
    model.eval()
    return model, preprocess, tokenizer

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data_dir", type=str, default="data/demo")
    ap.add_argument("--labels", type=str, default="tumor, stroma, background")
    args = ap.parse_args()

    os.makedirs("outputs", exist_ok=True)
    model, preprocess, tokenizer = load_model()
    texts = [s.strip() for s in args.labels.split(",")]
    text_tokens = tokenizer(texts)

    imgs = []
    paths = []
    for fname in os.listdir(args.data_dir):
        if fname.lower().endswith((".png",".jpg",".jpeg")):
            p = os.path.join(args.data_dir, fname)
            imgs.append(preprocess(Image.open(p).convert("RGB")))
            paths.append(p)
    if not imgs:
        print("No images found in data demo folder."); exit(0)

    with torch.no_grad():
        image_features = model.encode_image(torch.stack(imgs))
        text_features = model.encode_text(text_tokens)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        logits = image_features @ text_features.T
        preds = logits.argmax(dim=1).cpu().tolist()

    with open("outputs/zero_shot_results.txt","w") as f:
        for p, idx in zip(paths, preds):
            f.write(f"{p}	{texts[idx]}\n")
    print("Saved outputs/zero_shot_results.txt")
