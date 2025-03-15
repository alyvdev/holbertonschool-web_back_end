# Flask i18n Project

## Overview
This project demonstrates the implementation of internationalization (i18n) in a Flask web application. Internationalization allows a web application to be available in multiple languages, providing a better user experience for a global audience.

## Learning Objectives
- Parameterize Flask templates to display content in different languages
- Infer the correct locale based on URL parameters, user settings, or request headers
- Localize timestamps using Flask-Babel

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- First line of all files should be `#!/usr/bin/env python3`
- A `README.md` file at the root of the project is mandatory
- Code should use the pycodestyle style (version 2.5)
- All files must be executable
- All modules should have documentation
- All classes should have documentation
- All functions and methods should have documentation

## Installation
```bash
pip install Flask-Babel
```

## Usage
```bash
python app.py
```

## Tasks
- Basic Flask app setup
- Basic Babel setup
- Configuring available languages
- Force locale with URL parameter
- Determine best match locale
- Mock logging in
- Use user locale
- Translations with Babel
- Display the current time

## Resources
- [Flask-Babel Documentation](https://python-babel.github.io/flask-babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)