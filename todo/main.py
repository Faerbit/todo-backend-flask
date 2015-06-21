#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    response = Response("Hello World")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

def run():
    app.run()

if __name__ == "__main__":
    run()

