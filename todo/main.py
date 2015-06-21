#!/usr/bin/env python3

from flask import Flask, Response, jsonify
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")

@app.route("/")
def index():
    return "Hello World"

def run():
    app.run()

if __name__ == "__main__":
    run()

