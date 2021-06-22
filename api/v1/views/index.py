#!/usr/bin/python3
""" This is the blueprint file for status """

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


cls_dict = {
    "amentities": Amenity,
    "cities": City,
    "places": Place,
    "reviews": Review,
    "states": State,
    "users": User
}


@app_views.route('/stats')
def count_stat():
    count_dict = {}
    for k, v in cls_dict.items():
        count_dict[k] = storage.count(v)
    return jsonify(count_dict)


@app_views.route('/status')
def json_ify():
    return jsonify({"status": "OK"})
