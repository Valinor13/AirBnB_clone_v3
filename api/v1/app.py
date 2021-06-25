#!/usr/bin/python3
""" This module contains the flask drive """


import os
from models import storage
from flask import Flask, render_template, Blueprint, jsonify
from api.v1.views import app_views
from flask_cors import CORS


BNB3 = Flask(__name__)
BNB3.url_map.strict_slashes = False
CORS(BNB3, resources={r"/*": {"origins": "0.0.0.0"}})
BNB3.register_blueprint(app_views, url_prefix='/api/v1')


@BNB3.teardown_appcontext
def tear_down(error):
    if storage:
        storage.close()


@BNB3.errorhandler(404)
def custom_404(exception):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    if not os.getenv('HBNB_API_HOST'):
        os.environ['HBNB_API_HOST'] = '0.0.0.0'
    if not os.getenv('HBNB_API_PORT'):
        os.environ['HBNB_API_PORT'] = 5000
    BNB3.run(debug=True, host=os.getenv('HBNB_API_HOST'),
             port=os.getenv('HBNB_API_PORT'), threaded=True)
