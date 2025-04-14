from flask import Flask, request, jsonify
from flask_cors import CORS
from generator import generate_game_nft, validate_prompt_image, is_unique_image

app = Flask(__name__)

#  Enable CORS only for /generate endpoint from any origin (like Vercel)
CORS(app, resources={r"/generate": {"origins": "*"}})

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    img_path = generate_game_nft(prompt)
    valid, score = validate_prompt_image(prompt, img_path)
    unique = is_unique_image(img_path)

    return jsonify({
        "image_url": img_path,
        "similarity": score,
        "prompt_match": valid,
        "is_unique": unique
    })

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 80))  # Railway exposes clean URL on port 80
    app.run(host="0.0.0.0", port=port)
