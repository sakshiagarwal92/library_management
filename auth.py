from flask import request, jsonify

SECRET_TOKEN = "your-secret-token"

def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != SECRET_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper
