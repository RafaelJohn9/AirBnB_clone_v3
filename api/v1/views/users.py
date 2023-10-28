#!/usr/bin/python3

""" creates a new view for user objects
handles all default RESTFul api actions
"""
from flask import abort, request, jsonify
from api.v1.views import app_views
from models.user import User
from models import storage
methods = ['GET', 'POST', 'PUT', 'DELETE']


@app_views.route('/users', methods=methods)
def route_users():
    """ displays all users in the database """
    users = storage.all(User)
    userList = []

    if request.method == 'GET':
        for userId in users:
            obj = users[userId].to_dict()
            userList.append(obj)
        return jsonify(userList)
    elif request.method == 'POST':
        # creating a new instance
        try:
            newUser = request.get_json()
        except Exception:
            abort(400, description="Not a JSON")

        if newUser.get('email') is None:
            abort(400, description="Missing email")
        elif newUser.get('password') is None:
            abort(400, description="Missing password")
        else:
            newUser = User(**newUser)
            newUser.save()
            storage.reload()
            return jsonify(newUser.to_dict()), 201



@app_views.route('/users/', methods=methods)
@app_views.route('/users/<user_id>', methods=methods)
def route_users_id(user_id=None):
    """ routes for all users """
    users = storage.all(User)

    if user_id:
        key = f"User.{user_id}"

    if request.method == 'GET':
        if users.get(key):
            user = users[key].to_dict()
            return jsonify(user), 200
        else:
            abort(404)
    elif request.method == 'DELETE':
        if not users.get(key):
            abort(404)
        else:
            storage.delete(users[key])
            storage.save()
            return jsonify({}), 200
    elif request.method == 'PUT':
        if not users.get(key):
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
        user = users.get(key)
        for key, value in data.items():
            setattr(user, key, value)
        storage.save()
        storage.reload()
        return jsonify(user.to_dict()), 200
