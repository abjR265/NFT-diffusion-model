import os
import uuid
from PIL import Image
import torch
import clip
import imagehash
from diffusers import StableDiffusionPipeline

# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Lazy initialization
pipe = None
clip_model = None
clip_preprocess = None

def load_models():
    global pipe, clip_model, clip_preprocess
    if pipe is None:
        pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to(device)
    if clip_model is None:
        clip_model, clip_preprocess = clip.load("ViT-B/32", device=device)

def generate_game_nft(prompt):
    """
    Generate an image from a prompt and save it in the static/ folder
    Returns the filename (not the full path)
    """
    load_models()

    # Generate image
    image = pipe(prompt).images[0]

    # Generate unique filename and save to static/
    filename = f"{uuid.uuid4().hex}.png"
    save_path = os.path.join("static", filename)
    os.makedirs("static", exist_ok=True)
    image.save(save_path)

    return filename  # Only the filename (for public URL construction)

def validate_prompt_image(prompt: str, image_path: str, threshold: float = 0.3):
    """
    Validate if the image matches the prompt using CLIP similarity.
    """
    load_models()
    try:
        image = clip_preprocess(Image.open(image_path)).unsqueeze(0).to(device)
        text = clip.tokenize([prompt]).to(device)

        with torch.no_grad():
            image_features = clip_model.encode_image(image)
            text_features = clip_model.encode_text(text)

        similarity = torch.cosine_similarity(image_features, text_features).item()
        return similarity >= threshold, round(similarity, 3)
    except Exception as e:
        print(f"Validation error: {e}")
        return False, 0.0

def is_unique_image(image_path: str, history_dir: str = "assets", threshold: int = 10):
    """
    Check if the generated image is unique by comparing perceptual hashes.
    """
    try:
        current_hash = imagehash.phash(Image.open(image_path))
        os.makedirs(history_dir, exist_ok=True)

        for fname in os.listdir(history_dir):
            if fname.endswith(".png") and fname != os.path.basename(image_path):
                other_path = os.path.join(history_dir, fname)
                other_hash = imagehash.phash(Image.open(other_path))
                if abs(current_hash - other_hash) < threshold:
                    return False
        return True
    except Exception as e:
        print(f"Uniqueness check error: {e}")
        return False
