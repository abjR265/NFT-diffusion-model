from flask import Flask, request, jsonify, make_response, send_from_directory
from generator import generate_game_nft, validate_prompt_image, is_unique_image
import os

app = Flask(__name__)

@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return response

@app.route("/generate", methods=["POST", "OPTIONS"])
def generate():
    if request.method == "OPTIONS":
        # Preflight request handling
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return response, 204

    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Generate image and get filename (e.g., "abc123.png")
    filename = generate_game_nft(prompt)

    # Full image path for validation and uniqueness check
    full_image_path = os.path.join("static", filename)

    # Run CLIP validation + uniqueness check
    valid, score = validate_prompt_image(prompt, full_image_path)
    unique = is_unique_image(full_image_path)

    # Construct full public image URL
    base_url = request.host_url.rstrip("/")
    image_url = f"{base_url}/images/{filename}"

    return jsonify({
        "image_url": image_url,
        "similarity": score,
        "prompt_match": valid,
        "is_unique": unique
    })

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
