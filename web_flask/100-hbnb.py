#!/usr/bin/python3
"""
starts a Flask web application
 - Your web application must be listening on 0.0.0.0,
    port 5000
"""
from models import storage
from flask import Flask, render_template
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(Exception):
    """teardown"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
       - /hbnb route
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template(
          '100-hbnb.html',
          S_name='States',
          states=states,
          A_name='Amenities',
          amenities=amenities,
          P_name='Places',
          places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
