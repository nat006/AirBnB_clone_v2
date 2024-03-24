#!/usr/bin/python3

"""
This script starts a Flask web application with specific routes and requirements
"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when the root URL is visited
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Displays 'HBNB' when the /hbnb URL is visited
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Displays 'C ' followed by the value of the text variable with underscores replaced by spaces
    """
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    Displays 'Python ' followed by the value of the text variable with underscores replaced by spaces
    """
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Displays 'n is a number' only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with "Number: n" inside the <h1> tag in the body
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        return 'Not a valid integer'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
