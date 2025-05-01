from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from generator import generate_game_nft, validate_prompt_image, is_unique_image
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Manually add headers in case flask-cors doesn't catch cold-starts
@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    filename = generate_game_nft(prompt)
    full_image_path = os.path.join("static", filename)

    valid, score = validate_prompt_image(prompt, full_image_path)
    unique = is_unique_image(full_image_path)

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
<<<<<<< HEAD
    from os import environ
    port = int(environ.get("PORT", 10000))  
=======
    port = int(os.environ.get("PORT", 80))
>>>>>>> 766adf8550d8c04ccf7028a83b7042e25852c96e
    app.run(host="0.0.0.0", port=port)
