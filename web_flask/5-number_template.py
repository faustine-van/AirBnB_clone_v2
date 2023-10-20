#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
from flask import render_template
import re

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """starts a Flask web application:
       Routes:
           /: display “Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """starts a Flask web application:
       Routes:
         -  /hbnb: display “HBNB"
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def handleVarText(text):
    """starts a Flask web application:
       Routes:
        - /c/<text>: display “C ” followed by the value of the text variable
    """
    new_text = re.sub('_', ' ', text)
    return f'C {new_text}'


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """starts a Flask web application:
       Routes:
        - /python/<text>: display “Python ”, followed by the value of the text
          variable (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
    """
    new_text = re.sub('_', ' ', text)
    return f'C {new_text}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """starts a Flask web application:
       Routes:
          - /number/<n>: display “n is a number” only if n is an integer
    """
    if isinstance(n, int):
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """starts a Flask web application:
       Routes:
          - /number_template/<n>: display a HTML page only if n is an integer:
          - H1 tag: “Number: n” inside the tag BODY
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    # python3 -m web_flask.0-hello_route
    app.run(debug=True, host="0.0.0.0", port=5000)
