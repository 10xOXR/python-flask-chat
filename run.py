import os
from flask import Flask, redirect, render_template, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_messages(username, message):
    # Adds messages to the 'messages' list
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))

def get_all_messages():
    # Get all of hte messages and separate them using '<br>' tags
    return "<br>".join(messages)

@app.route("/", methods = ["GET", "POST"])
def index():
    # Main page with instructions
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

@app.route("/<username>")
def user(username):
    # Displays Username and messages
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

@app.route("/<username>/<message>")
def send_message(username, message):
    # Takes username and message from URL and diplays in browser.
    add_messages(username, message)
    return redirect(username)

app.run(host=os.getenv("IP"), port=os.getenv("PORT"), debug=True)