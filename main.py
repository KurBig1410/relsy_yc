from flask import Flask, jsonify
from flask_cors import CORS
import json
from run import run_pipeline
import subprocess
import asyncio

from data_base.engine import create_db


app = Flask(__name__)
CORS(app)  # Разрешаем CORS для фронтенда


@app.route("/api/run", methods=["GET"])
def run_parser():
    try:
        # путь до скрипта
        command = ["xvfb-run", "-a", "python3", "run.py"]  # или main.py

        # запускаем как подпроцесс
        result = subprocess.run(command, capture_output=True, text=True, timeout=300)

        if result.returncode == 0:
            return jsonify({"status": "success", "output": result.stdout})
        else:
            return (
                jsonify(
                    {
                        "status": "error",
                        "code": result.returncode,
                        "stderr": result.stderr,
                    }
                ),
                500,
            )

    except Exception as e:
        return jsonify({"status": "failed", "error": str(e)}), 500


@app.route("/api/ping")
def ping():
    return jsonify({"status": "ok"})


@app.route("/api/data", methods=["GET"])
def get_data():
    with open("data/response_out.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == "__main__":
    asyncio.run(create_db())  # создаём БД
    app.run(host="0.0.0.0", port=5000, debug=True)
