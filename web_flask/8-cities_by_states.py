#!/usr/bin/python3
"""
starts a Flask web application
 - Your web application must be listening on 0.0.0.0,
    port 5000
"""
import os
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(Exception):
    """ remove the current SQLAlchemy Session  """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
         cities_by_states
    """
    states = storage.all('State')

    # An empty dict to store all cities
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
