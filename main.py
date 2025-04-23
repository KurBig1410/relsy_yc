from flask import Flask, jsonify
from flask_cors import CORS
import json
from run import start

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для фронтенда

@app.route("/api/data", methods=["GET"])
def get_data():
    start()
    with open("data/response_out.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)