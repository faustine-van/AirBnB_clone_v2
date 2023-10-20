#!/usr/bin/python3
"""starts a Flask web application"""
from web_flask import app


@app.route('/', strict_slashes=False)
def hello():
    """starts a Flask web application:
       Routes:
           /: display “Hello HBNB!
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    # python3 -m web_flask.0-hello_route
    app.run(debug=True, host="0.0.0.0", port=5000)
