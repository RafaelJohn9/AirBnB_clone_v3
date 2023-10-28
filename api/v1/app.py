#!/usr/bin/python3

""" this is my REST api creation """

from api.v1.views import app_views
from flask import Flask, make_response
from models import storage
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """ teardown method for closing an instance """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response({"error": "Not found"}, 404)


if __name__ == "__main__":
    """ get host and port from env var """
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
