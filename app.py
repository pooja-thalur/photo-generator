# app.py
from flask import Flask, request, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
CORS(app)

# Load db.json once at startup
with open("db.json", "r", encoding="utf-8") as f:
    db = json.load(f)
photos = db.get("photos", [])

@app.route("/")
def index():
    return "Welcome to the Photo API! Use /photos to access photo data."

@app.route("/photos")
def get_photos():
    # Query params
    try:
        start = int(request.args.get("_start", 0))
        limit = int(request.args.get("_limit", 100))
    except ValueError:
        return jsonify({"error": "Invalid _start or _limit"}), 400

    end = start + limit
    sliced = photos[start:end]

    # Pagination metadata
    total = len(photos)
    next_start = end if end < total else None
    prev_start = start - limit if start - limit >= 0 else None

    return jsonify({
        "data": sliced,
        "paging": {
            "total": total,
            "start": start,
            "limit": limit,
            "next": f"/photos?_start={next_start}&_limit={limit}" if next_start is not None else None,
            "prev": f"/photos?_start={prev_start}&_limit={limit}" if prev_start is not None else None
        }
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
