from flask import Flask, render_template, session, request, send_from_directory
from flask_session import Session

app = Flask(__name__, static_url_path='')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    #session["tasks"] = []
    if session.get("tasks") is None:
        session["tasks"] = []
    if request.method == "POST" and request.form.get("task") != '' and request.form.get("task") is not None:
        task = request.form.get("task")
        session["tasks"].append(task)
    return render_template("todolist.html", tasks=session["tasks"])
