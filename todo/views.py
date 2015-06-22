from todo import app

from flask import jsonify, request, url_for
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
        return jsonify(construct_dict(entry))
    else:
        if request.method == "DELETE":
            Entry.query.delete()
            db_session.commit()
        response = []
        for entry in Entry.query.all():
            response.append(construct_dict(entry))
        return json.dumps(response)

@app.route("/<int:entry_id>", methods=["GET", "PATCH"])
def entry(entry_id):
    if request.method == "PATCH":
        request_json = request.get_json()
        entry = Entry.query.filter(Entry.id == entry_id).first()
        entry.title = request_json["title"]
        db_session.commit()
    return jsonify(construct_dict(Entry.query.filter(Entry.id == entry_id).first()))

def construct_dict(entry):
    return dict(title=entry.title, completed=entry.completed,
            url=url_for("entry", entry_id=entry.id, _external=True))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
