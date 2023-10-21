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
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
     - /states_list: display a HTML page: (inside the tag BODY)
       - H1 tag: “States”
         - UL tag: with the list of all State objects present
             in DBStorage sorted by name (A->Z) tip
         - LI tag: description of one State: <state.id>: <B><state.name></B>
    """
    states = storage.all('State')
    all_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
