import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    # Adds messages to the 'messages' list
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    # Get all of hte messages and separate them using '<br>' tags
    return "<br>".join(messages)

@app.route("/")
def index():
    # Main page with instructions
    return "To send a message, use the format /USERNAME/MESSAGE"

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