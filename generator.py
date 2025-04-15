import os
from PIL import Image
import torch
import clip
import imagehash
from diffusers import StableDiffusionPipeline

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Stable Diffusion pipeline with error handling
try:
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to(device)
except Exception as e:
    print(f"[❌] Error loading Stable Diffusion: {e}")
    pipe = None

# Load CLIP model with error handling
try:
    clip_model, clip_preprocess = clip.load("ViT-B/32", device=device)
except Exception as e:
    print(f"[❌] Error loading CLIP model: {e}")
    clip_model, clip_preprocess = None, None


def generate_game_nft(prompt, save_path="generated_asset.png"):
    if pipe is None:
        raise RuntimeError("Stable Diffusion pipeline not loaded.")
    try:
        image = pipe(prompt).images[0]
        image.save(save_path)
        return save_path
    except Exception as e:
        print(f"[❌] Image generation error: {e}")
        raise


def validate_prompt_image(prompt: str, image_path: str, threshold: float = 0.3):
    if clip_model is None or clip_preprocess is None:
        print("[⚠️] CLIP model not loaded.")
        return False, 0.0
    try:
        image = clip_preprocess(Image.open(image_path)).unsqueeze(0).to(device)
        text = clip.tokenize([prompt]).to(device)

        with torch.no_grad():
            image_features = clip_model.encode_image(image)
            text_features = clip_model.encode_text(text)

        similarity = torch.cosine_similarity(image_features, text_features).item()
        return similarity >= threshold, round(similarity, 3)
    except Exception as e:
        print(f"[❌] Validation error: {e}")
        return False, 0.0


def is_unique_image(image_path: str, history_dir: str = "assets", threshold: int = 10):
    try:
        current_hash = imagehash.phash(Image.open(image_path))

        if not os.path.exists(history_dir):
            os.makedirs(history_dir)

        for fname in os.listdir(history_dir):
            if fname.endswith(".png") and fname != os.path.basename(image_path):
                other_path = os.path.join(history_dir, fname)
                other_hash = imagehash.phash(Image.open(other_path))
                if abs(current_hash - other_hash) < threshold:
                    return False
        return True
    except Exception as e:
        print(f"[❌] Uniqueness check error: {e}")
        return False
