import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv() #the jon is this to get the env file pb

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello</h1>"


@app.route("/<random_string>")
def return_backward_string(random_string):
    return "".join(reversed(random_string))


@app.route("/get-mode")
def get_mode():
    return os.environ.get("MODE")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
