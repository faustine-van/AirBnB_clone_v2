#!/usr/bin/python3
"""starts a Flask web application"""

from web_flask import app

@app.route('/', strict_slashes=False)
def home():
    """starts a Flask web application:
       Routes:
           1./: display “Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """starts a Flask web application:
       Routes:
           1./hbnb: display “Hello HBNB!
    """
    return 'HBNB'


if __name__ == "__main__":
    # python3 -m web_flask.0-hello_route
    app.run(host="0.0.0.0", port=5000)
