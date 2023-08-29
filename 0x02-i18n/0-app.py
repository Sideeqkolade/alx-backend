#!/usr/bin/env python3
"""A flask setup"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def show_page():
    """returns the index.html page"""
    return render_template('index.html')


app.run(debug=True)
