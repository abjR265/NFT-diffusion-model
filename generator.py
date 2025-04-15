# -*- coding: utf-8 -*-
"""generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qnSFXNe1NgAjTdP4DMrjA7a3pSzkObkw
"""

from diffusers import StableDiffusionPipeline
import torch

# Load pretrained Stable Diffusion
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_game_nft(prompt, save_path="generated_asset.png"):
    image = pipe(prompt).images[0]
    image.save(save_path)
    return save_path

generate_game_nft("Legendary dragon-themed sword with electric effects, 4k, game concept art")

import json

def generate_metadata(name, traits):
    metadata = {
        "name": name,
        "description": "In-game asset NFT for a fantasy battle game.",
        "image": f"{name}.png",
        "attributes": [{"trait_type": k, "value": v} for k, v in traits.items()]
    }
    with open(f"{name}.json", "w") as f:
        json.dump(metadata, f, indent=2)

generate_metadata("Thunderblade", {
    "Power": "Electric",
    "Tier": "Legendary",
    "Glow": "Blue",
    "Type": "Sword"
})


import os
import shutil

# Create /mnt/data/ if needed
os.makedirs("/mnt/data", exist_ok=True)

# Copy the image
shutil.copy("generated_asset.png", "/mnt/data/image.png")
print("✅ Copied to /mnt/data/image.png")

!pip install git+https://github.com/openai/CLIP.git
!pip install imagehash

# ✅ Step 2: Import Libraries
import os
from PIL import Image
import torch
import clip
import imagehash

# ✅ Step 3: Load CLIP Model
device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model, clip_preprocess = clip.load("ViT-B/32", device=device)



#  Define Validator Functions

def validate_prompt_image(prompt: str, image_path: str, threshold: float = 0.3):
    """
    Check how well the image matches the prompt using CLIP.
    Returns (True/False, similarity_score)
    """
    try:
        image = clip_preprocess(Image.open(image_path)).unsqueeze(0).to(device)
        text = clip.tokenize([prompt]).to(device)

        with torch.no_grad():
            image_features = clip_model.encode_image(image)
            text_features = clip_model.encode_text(text)

        similarity = torch.cosine_similarity(image_features, text_features).item()
        return similarity >= threshold, round(similarity, 3)
    except Exception as e:
        print(f"Error during prompt-image validation: {e}")
        return False, 0.0


def is_unique_image(image_path: str, history_dir: str = "assets", threshold: int = 10):
    """
    Check if the image is unique compared to existing ones in the history folder.
    Uses perceptual hashing.
    """
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
        print(f"Error during uniqueness check: {e}")
        return False

# Validate the generated image
image_path = "/mnt/data/image.png"
prompt = "Legendary dragon-themed sword with electric effects, 4k, game concept art"

valid_prompt, similarity = validate_prompt_image(prompt, image_path)
is_unique = is_unique_image(image_path)

print(f"🔍 Prompt Match: {valid_prompt} | Similarity Score: {similarity}")
print(f"🎯 Unique Image: {is_unique}")

if valid_prompt and is_unique:
    print("✅ NFT passed validation. Ready to mint.")
else:
    print("❌ NFT failed validation. Please try a new prompt.")

import shutil
os.makedirs("assets", exist_ok=True)

# Move image and metadata
shutil.copy(image_path, "assets/Thunderblade.png")
shutil.copy("Thunderblade.json", "assets/Thunderblade.json")

