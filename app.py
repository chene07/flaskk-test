from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        print("Username:", username)
        print("Password:", password)

        msg = "Form submitted!"

    return render_template("login.html", msg=msg)

@app.route("/test-template")
def test_template():
    return render_template("login.html")  # Try to load just the template

