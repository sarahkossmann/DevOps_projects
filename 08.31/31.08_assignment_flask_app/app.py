import os
from flask import Flask, Request, Response, render_template, send_from_directory, request, jsonify
from sys import path

# 9. Create a Flask application which listens to port 30000 and has 2 routes:
# a. /content - which returns the content of any txt file and status code 200 (e.g:
# localhost:4000/content).
# b. /register - which writes the word “hello” into any txt file and return “success” and
# status code 201 as a response (e.g: localhost:4000/register).

# to run my Flask app on port 3000 : flask run -h localhost -p 3000
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
text_file = os.path.join(basedir, "file.txt")


@app.route('/')
def home():
    return '<h1>This is the home page</h1>'

@app.route('/content')
def content():
    WORDS = []
    with open(text_file, "r") as file:
        for line in file.readlines():
            WORDS.append(line.rstrip())
    words = [word for word in WORDS]
    return jsonify(words)

@app.route('/register')
def register():
    with open(text_file, "a+") as f:
        f.write("\nhello")
    return Response('Success', status=201)

if __name__ == "__main__":
    app.run()