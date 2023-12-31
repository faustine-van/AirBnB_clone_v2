#!/usr/bin/python3
"""
starts a Flask web application
 - Your web application must be listening on 0.0.0.0,
    port 5000
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(Exception):
    """ remove the current SQLAlchemy Session  """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id=None):
    """
         cities_by_states
    """
    states = storage.all('State')
    if not id:
        return render_template(
                '9-states.html',
                name='States',
                states=states)
    # state=next((state for state in states.values() if state.id==id), None)
    state = None
    for state_obj in states.values():
        if state_obj.id == id:
            state = state_obj
            break
    if state:
        cities = state.cities
        return render_template(
            '9-states.html',
            state=state, cities=cities, not_found=False
        )
    else:
        return render_template('9-states.html', not_found=True), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
