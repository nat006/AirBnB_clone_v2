#!/usr/bin/python3
"""
This module starts a Flask web application that listens on 0.0.0.0, port 5000
"""

from flask import Flask
from re import sub

app = Flask(name)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' when accessing the root route
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB' when accessing the /hbnb route
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by the value of the text variable (replace underscores with spaces)
    """
    text = sub('_', ' ', text)
    return 'C {}'.format(text)

if name == 'main':
    app.run(host='0.0.0.0', port=5000)
