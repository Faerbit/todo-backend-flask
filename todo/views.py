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
        return jsonify(title=request_json["title"], completed="")
    else:
        if request.method == "DELETE":
            Entry.query.delete()
            db_session.commit()
        response = "["
        all_entries = Entry.query.all()
        if all_entries:
            for entry in all_entries[:-1]:
                response += construct_json(entry)
                response += ", "
            response += construct_json(all_entries[-1])
        response += "]"
        return response

def construct_json(entry):
    return json.dumps(dict(title=entry.title,completed=""))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
