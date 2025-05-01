# Non-Fungible Token (NFT) Generator & Validator using AI Diffusion Model

[Live Demo ➝[ https://nft-diffusion-model.vercel.app ]

A full-stack application that allows users to generate unique AI NFTs using text prompts, validate them using CLIP relevance and image hashing, and explore featured artworks. Built with Next.js, Tailwind CSS, Replicate API, and deployed via Vercel (frontend) and Render (Flask backend).

---

## Features

- Text-to-Image Generation using Stable Diffusion via Replicate API
- Prompt Relevance Scoring using OpenAI CLIP
- Image Uniqueness Check using perceptual hashing
- Dynamic Gallery for featured NFTs
- Modern single-scroll UI styled like a gaming NFT marketplace

---

## Tech Stack

**Frontend**
- Next.js 14
- Tailwind CSS
- TypeScript
- Vercel

**Backend (Deprecated)**
- Flask
- CLIP (OpenAI)
- imagehash
- Render

**AI Generation**
- Replicate API (Stable Diffusion)

---

## How It Works

1. User enters a prompt (e.g., "Cyberpunk Samurai on Mars")
2. Image is generated using Replicate’s Stable Diffusion
3. CLIP validates prompt-image similarity
4. ImageHash ensures image uniqueness
5. Valid NFTs are shown in the Featured Gallery

---

## Local Development

### Prerequisites

- Node.js 18+
- Python 3.9+
- Replicate API Token

### Setup

```bash
# Clone the repo
git clone https://github.com/abjR265/NFT-diffusion-model.git
cd ai-nft-generator

# Install frontend dependencies
npm install

# Setup environment
echo "REPLICATE_API_TOKEN=your_token_here" > .env.local

# Run development server
npm run dev
```

Legacy backend (no longer required):
```bash
pip install -r requirements.txt
python app.py
```

---

## Environment Variables

| Variable               | Description                          |
|------------------------|--------------------------------------|
| REPLICATE_API_TOKEN    | Your Replicate API key               |

---

## Validation Logic

- Prompt-Image Relevance:
  Uses CLIP to ensure cosine similarity between image and prompt is above threshold (e.g., 0.25)
- Image Uniqueness:
  Uses perceptual hashing via imagehash. Duplicates rejected.

---

## Deployment

### Frontend (Vercel)
```bash
vercel --prod
```

### Backend (Legacy: Render)
```bash
# Deploy manually via render.com dashboard
```

---

## Authors

- Abhijay Rane (ar2536@cornell.edu)

---
