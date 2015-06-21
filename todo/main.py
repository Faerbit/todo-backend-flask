#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

def run():
    app.run()

if __name__ == "__main__":
    run()

