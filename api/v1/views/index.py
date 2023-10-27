#!/usr/bin/python3

""" creates a route /status on the object
app_views that returns a JSON"""

from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route("status", strict_slashes=False)
def route_views():
    """ this the route for the status code """
    return jsonify({"status": "OK"})
