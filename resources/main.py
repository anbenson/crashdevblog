import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

# app configuration
app = Flask(__name__)
app.debug = True
PORT = 8080

# rudimentary, hacky database
blogEntries = [] # this is a time-ordered MRU list of "entries"

# helper functions
def findUTCTimeString():
  currDT = datetime.utcnow()
  return currDT.strftime("%I:%M %p (UTC) %b %d, %Y")

def createEntry(author, title, text):
  return {"author": author,
          "title": title,
          "text": text,
          "datetime": findUTCTimeString()}

# routing
@app.route("/")
def homePage():
  return "Hello World!"

# start the app if we're directly running this file
if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = PORT)
