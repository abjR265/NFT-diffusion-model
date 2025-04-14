from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from generator import generate_game_nft, validate_prompt_image, is_unique_image

app = Flask(__name__)
# Apply CORS to the entire app with appropriate settings
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "Content-Type,Authorization", "methods": ["POST", "OPTIONS"]}})

@app.route("/generate", methods=["POST", "OPTIONS"])
def generate():
    # Handle preflight OPTIONS request
    if request.method == "OPTIONS":
        return make_response('', 204)
    
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
    port = int(environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
