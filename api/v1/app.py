#!/usr/bin/python3


import os
from models import storage
from flask import Flask, render_template, Blueprint
from api.v1.views import app_views


BNB3 = Flask(__name__)
BNB3.url_map.strict_slashes = False
BNB3.register_blueprint(app_views, url_prefix='/api/v1')


@BNB3.teardown_appcontext
def tear_down(error):
    if storage:
        storage.close()

if __name__ == '__main__':
    if not os.getenv('HBNB_API_HOST'):
        os.environ['HBNB_API_HOST'] = '0.0.0.0'
    if not os.getenv('HBNB_API_PORT'):
        os.environ['HBNB_API_PORT'] = 5000
    BNB3.run(debug=True, host=os.getenv('HBNB_API_HOST'),
             port=os.getenv('HBNB_API_PORT'), threaded=True)
