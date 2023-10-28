#!/usr/bin/python3

""" creates a new view for amenity objects
handles all default RESTFul api actions
"""
from flask import abort, request, jsonify
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage


methods = ['GET', 'POST', 'PUT', 'DELETE']


@app_views.route('/amenities', methods=methods)
def route_amenities():
    """ displays all amenities in the database """
    amenities = storage.all(Amenity)
    amenityList = []

    if request.method == 'GET':
        for amenityId in amenities:
            obj = amenities[amenityId].to_dict()
            amenityList.append(obj)
        return jsonify(amenityList)
    elif request.method == 'POST':
        # creating a new instance
        try:
            newAmenity = request.get_json()
        except Exception:
            abort(400, description="Not a JSON")

        if newAmenity.get('name') is None:
            abort(400, description="Missing name")
        else:
            newAmenity = Amenity(**newAmenity)
            newAmenity.save()
            storage.reload()
            return jsonify(newAmenity.to_dict()), 201


@app_views.route('/amenities/', methods=methods)
@app_views.route('/amenities/<amenity_id>', methods=methods)
def route_amenities_id(amenity_id=None):
    """ routes for all amenities """
    amenities = storage.all(Amenity)

    if amenity_id:
        key = f"Amenity.{amenity_id}"

    if request.method == 'GET':
        if amenities.get(key):
            amenity = amenities[key].to_dict()
            return jsonify(amenity), 200
        else:
            abort(404)
    elif request.method == 'DELETE':
        if not amenities.get(key):
            abort(404)
        else:
            storage.delete(amenities[key])
            storage.save()
            return jsonify({}), 200
    elif request.method == 'PUT':
        if not amenities.get(key):
            abort(404)
        try:
            data = request.get_json()
        except Exception:
            abort(400, description="Not a JSON")
        # checking for exceptions of updates
        if data.get('id'):
            del(data['id'])
        if data.get('created_at'):
            del(data['created_at'])
        if data.get('updated_at'):
            del(data['updated_at'])
        # end for exceptions of updates
        amenity = amenities.get(key)
        for key, value in data.items():
            setattr(amenity, key, value)
        storage.save()
        storage.reload()
        return jsonify(amenity.to_dict()), 200
