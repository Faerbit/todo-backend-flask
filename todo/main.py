#!/usr/bin/env python3

import os
from flask import Flask, Response, jsonify, request
from flask import json
from flask.ext.cors import CORS

DATABASE=os.getenv("DATABASE_URL", "sqlite://")
DATABASE=DATABASE.strip()

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")

# placed down here to prevent circular imports
# messing up things
from todo.database import db_session
from todo.models import Entry

@app.route("/", methods=["GET", "POST", "DELETE"])
def index():
    if request.method == "POST":
        request_json = request.get_json()
        entry = Entry(request_json["title"])
        db_session.add(entry)
        db_session.commit()
        return jsonify(title=request_json["title"])
    else:
        response = "["
        for entry in Entry.query.all():
            response += json.dumps(dict(title=entry.title))
        response += "]"
        return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

def run():
    app.run()

if __name__ == "__main__":
    run()

