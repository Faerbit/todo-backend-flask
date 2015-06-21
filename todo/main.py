#!/usr/bin/env python3

import os
from flask import Flask, Response, jsonify
from flask.ext.cors import CORS

DATABASE=os.getenv("DATABASE_URL", "sqlite://")

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")

@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify(string="Hello World")

def run():
    app.run()

if __name__ == "__main__":
    run()

