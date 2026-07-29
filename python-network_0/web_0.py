#!/usr/bin/python3
""" Web server
"""
from flask import Flask, request
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """ Root
    """
    if request.headers.get('X-School-User-Id', "0") == "98":
        return "OK"
    else:
        return "NOP"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
