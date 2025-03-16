#!/usr/bin/env python3
"""Flask app with internationalization support"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Returns a user dictionary or None if ID cannot be found
    or if login_as was not passed"""
    user_id = request.args.get('login_as')
    if user_id:
        try:
            return users.get(int(user_id))
        except (ValueError, KeyError):
            return None
    return None


@app.before_request
def before_request():
    """Sets the user as a global on flask.g.user"""
    g.user = get_user()


def get_locale():
    """Determine the best match for supported languages based on priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    # Priority 1: Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Priority 2: Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Priority 3: Locale from request header
    # Priority 4: Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """Determine the best match for timezone based on priority:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default to UTC
    """
    # Priority 1: Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    # Priority 2: Timezone from user settings
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except UnknownTimeZoneError:
            pass

    # Priority 3: Default timezone (UTC)
    return app.config['BABEL_DEFAULT_TIMEZONE']


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/', strict_slashes=False)
def index():
    """Route for the home page"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
