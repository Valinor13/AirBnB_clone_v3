#!/usr/bin/python3
""" Retrieves a list of all State objects"""

from flask import Flask, Blueprint, render_template
from flask import request, url_for, redirect, abort, jsonify, json
from models.state import State
from models.amenities import Amenity
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage


@app_views.route('/amenity', methods=['GET', 'POST'])
def all_amenity():
    if request.method == "GET":
        all_amenities = storage.all(Amenity)
        list_of_dicts = []
        for values in all_amenities.values():
            list_of_dicts.append(BaseModel.to_dict(values))
        return jsonify(list_of_dicts)
    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        if 'name' not in json_dict.keys():
            abort(400, 'Missing name')
        else:
            new_amenity = Amenity(name=json_dict['name'])
            new_amenity.save()
            return jsonify(BaseModel.to_dict(new_amenity)), 201


@app_views.route('/amenity/<amenity_id>', methods=['GET', 'DELETE', 'PUT'])
def amenity_by_id(amenity=id=None):
    all_amenity = storage.all(Amenity)
    sig = 0
    for key in all_amenity.keys():
        if amenity_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        return jsonify(BaseModel.to_dict(all_amenity[key]))

    elif request.method == "DELETE":
        all_amenity[key].delete()
        storage.save()
        return jsonify({}), 200

    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        for k, v in json_dict.items():
            if k == 'id' or k == 'created_at' or k == 'updated_at':
                continue
            else:
                setattr(all_amenity[key], k, v)
        all_amenity[key].save()
        return jsonify(BaseModel.to_dict(all_amenity[key])), 200
