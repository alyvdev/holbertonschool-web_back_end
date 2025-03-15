#!/usr/bin/env python3
"""Create a simple Flask app."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    return render_template('/templates/index.html')
