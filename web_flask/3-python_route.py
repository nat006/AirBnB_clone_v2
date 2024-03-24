#!/usr/bin/python3

"""
This module starts a Flask web application that listens on 0.0.0.0:5000
"""

from flask import Flask
from markupsafe import escape

app = Flask(name)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function displays 'Hello HBNB!' when the root URL is visited
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    This function displays 'HBNB' when the /hbnb URL is visited
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    This function displays 'C ' followed by the value of the text variable when /c/<text> is visited
    """
    return 'C {}'.format(escape(text).replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    This function displays 'Python ' followed by the value of the text variable when /python/<text> is visited
    """
    return 'Python {}'.format(escape(text).replace('_', ' '))

if name == 'main':
    app.run(host='0.0.0.0', port=5000)
