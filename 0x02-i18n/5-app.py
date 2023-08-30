#!/usr/bin/env python3
"""A flask app and babel class"""
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Union, Dict

class Config:
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    else:
        return None


@app.before_request
def before_request() -> None:
    """get a user if any"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Translates to the best match language"""
    locale = request.args.get('locale')

    # Check if the 'locale' query parameter is present in the request
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """returns the index.html page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
