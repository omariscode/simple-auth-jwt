from functools import wraps
from flask import request, jsonify
from ..jwt_handler import decode_token


def auth_middleware(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Missing token"}), 401

        token = token.split()[1]

        decode_token(token)

        return f(*args, **kwargs)
    return wrapper