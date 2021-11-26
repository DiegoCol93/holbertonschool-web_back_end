#!/usr/bin/env python3
""" Basic Flask application. """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root() -> render_template:
    """ Root route of the application. """
    return render_template("0-index.html")
