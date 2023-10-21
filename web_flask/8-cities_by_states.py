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
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
      - H1 tag: “States”
        - UL tag: with the list of all State objects present 
            in DBStorage sorted by name (A->Z) tip
         - LI tag: description of one State: <state.id>: 
               <B><state.name></B> + UL tag: with the list
              of City objects linked to the State sorted by name (A->Z)
          - LI tag: description of one City: <city.id>: <B><city.name></B>
    """
    states = storage.all('State')
    all_states = sorted(states.values(), key=lambda state: state.name)

    # An empty dict to store all cities
    citiesByState = {}
    for state in all_states:
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Use the cities relationship if using DBStorage
            cities = state.cities
        else:
            # Use the public getter method if not using DBStorage
            cities = state.cities()
        cities = sorted(cities, key=lambda city: city.name)
        citiesByState[state] = cities
    return render_template('8-cities_by_states.html', citiesByState=citiesByState)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
