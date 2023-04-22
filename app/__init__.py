from flask import Flask, render_template
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    pass
