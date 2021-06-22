#!/usr/bin/python3
import app_views from api.va.views
from flask import jsonify
@app_views.route('/status')
def json_ify():
    return jsonify("status": "OK")
