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
        return jsonify(title=request_json["title"], completed=False, url="")
    else:
        if request.method == "DELETE":
            Entry.query.delete()
            db_session.commit()
        response = []
        for entry in Entry.query.all():
            response.append(dict(title=entry.title, completed=entry.completed, url=""))
        return json.dumps(response)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
