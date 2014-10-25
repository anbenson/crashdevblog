import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

# app configuration
app = Flask(__name__)
app.debug = True
PORT = 8080

# rudimentary, hacky database
blogEntries = [] # this is a time-ordered list of "entries"

def findUTCTimeString():
  currDT = datetime.utcnow()
  return currDT.strftime("%I:%M %p (UTC) %b %d, %Y")

def createEntry(author, title, text):
  return {"author": author,
          "title": title,
          "text": text,
          "datetime": findUTCTimeString()}

class Entry(object):
  def __init__(self, author, title, text):
    self.author = author
    self.title = title
    self.text = text
    self.date = datetime.utcnow()

# routing
@app.route("/")
def homePage():
  return render_template("index.html", entries = blogEntries)

@app.route("/about")
def aboutPage():
  return render_template("about.html")

@app.route("/create")
def createPage():
  return render_template("create.html")

@app.route("/newpost", methods=["POST"])
def newpost():
  author = request.form["author"]
  title = request.form["title"]
  text = request.form["text"]
  blogEntries.insert(0, createEntry(author, title, text))
  return redirect(url_for("homePage"))

@app.route("/refreshEntries")
def refreshEntries():
  return json.dumps(blogEntries)

# start the app if we're directly running this file
if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = PORT)
