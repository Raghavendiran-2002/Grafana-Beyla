from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.before_request
def log_request_info():
    app.logger.info(f"Request: {request.method} {request.path}")

@app.after_request
def log_response_info(response):
    app.logger.info(f"Response: {response.status}")
    return response

@app.route("/")
def hello():
    return "Hello from Grafana Beyla!"

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
