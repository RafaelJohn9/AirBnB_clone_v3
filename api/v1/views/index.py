#!/usr/bin/python3

""" creates a route /status on the object
app_views that returns a JSON"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place


@app_views.route("status", strict_slashes=False)
def route_status():
    """ this the route for the status code """
    return jsonify({"status": "OK"})


@app_views.route("stats", strict_slashes=False)
def route_stats():
    """ an endpoint that retrieves the num of each object type """
    from models import storage
    facilities = {'amenities': Amenity,
                 'cities': City,
                 'places': Place,
                 'reviews': Review,
                 'states': State,
                 'users': User
                 }
    returnDict = {}
    for facility in facilities:
        count = storage.count(facilities[facility])
        returnDict[facility] = count

    return jsonify(returnDict)
