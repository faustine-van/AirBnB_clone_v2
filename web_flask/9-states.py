#!/usr/bin/python3
"""
starts a Flask web application
 - Your web application must be listening on 0.0.0.0,
    port 5000
"""
import os
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(Exception):
    """ remove the current SQLAlchemy Session  """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """
     - /statest route
    """
    states = storage.all('State')
    all_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(
                           '9-states.html',
                           all_states=all_states,
                           page='states')


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id):
    """
         cities_by_states
    """
    states = storage.all()
    state = next((state for state in states.values() if state.id == id), None)
    if state:
        cities = state.cities
        # An empty dict to store all cities
        return render_template(
            '9-states.html', state=state, cities=cities
        )
    else:
        return render_template('9-states.html', not_found=True), 404


@app.errorhandler(404)
def PageNotFound(error):
    """  404 page """
    return render_template('9-states.html', not_found=True), 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
