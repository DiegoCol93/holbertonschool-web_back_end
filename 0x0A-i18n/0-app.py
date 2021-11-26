#!/usr/bin/env python3
""" Basic Flask application. """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/', methods["GET"])
def root() -> str:
    """ Root route of the application. """
    return render_template("0-index.html")
