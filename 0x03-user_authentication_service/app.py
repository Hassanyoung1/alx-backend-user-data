#!/usr/bin/env python
"""
flask app
"""

from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Return json respomse
    {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """
    user route
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    """
    Main function
    """
    app.run(host="0.0.0.0", port="5000")
