#!/usr/bin/python3
"""
This module starts a Flask web application that listens on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(name)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' when accessing the root route
    """
    return 'Hello HBNB!'

if name == 'main':
    app.run(host='0.0.0.0', port=5000)
