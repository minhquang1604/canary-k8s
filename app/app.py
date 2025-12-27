from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hi from version {os.getenv('VERSION', 'unknown')}"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

