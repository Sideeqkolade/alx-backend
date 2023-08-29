#!/usr/bin/env python3
"""A flask app and babel class"""
from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__)


class Config:
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """a function that best matches the language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """returns the index.html page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
