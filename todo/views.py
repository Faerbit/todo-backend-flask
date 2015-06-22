from todo import app

from flask import jsonify, request
from flask import json

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
        if request.method == "DELETE":
            Entry.query.delete()
        response = "["
        all_entries = Entry.query.all()
        if all_entries:
            for entry in all_entries[:-1]:
                response += json.dumps(dict(title=entry.title))
                response += ", "
            response += json.dumps(dict(title=all_entries[-1].title))
        response += "]"
        return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
