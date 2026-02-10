from flask import Flask, jsonify, request
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Hello from ACS Simple App 🚀",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "staging"),
        "time": datetime.utcnow().isoformat()
    })

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    text = data.get("message", "no message provided")

    return jsonify({
        "echo": text,
        "length": len(text)
    })

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",   # WAJIB untuk Docker
        port=5000,
        debug=False
    )
