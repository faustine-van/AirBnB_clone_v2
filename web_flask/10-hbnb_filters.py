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
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
       - /hbnb_filters route
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template(
          '10-hbnb_filters.html',
          S_name='States',
          states=states,
          A_name='Amenities',
          amenities=amenities)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
