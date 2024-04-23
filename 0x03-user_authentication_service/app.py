#!/usr/bin/env python
"""
flask app
"""

from flask import Flask, request, jsonify
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    index route
    """
    message = {"message": "Bienvenue"}
    return jsonify(message)



@app.route("/users", methods=["POST"], strict_slashes=False)
def userse(email: str, password: str):
    """
    user route
    """
    try:
    email = request.form.get("email")
    password = request.form.get("password")



if __name__ == "__main__":
    """
    Main function
    """
    app.run(host="0.0.0.0", port="5000")
