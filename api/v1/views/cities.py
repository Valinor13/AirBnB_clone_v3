#!/usr/bin/python3
""" Retrieves a list of all City objects"""

from flask import Flask, Blueprint, render_template
from flask import request, url_for, redirect, abort, jsonify, json
from models.state import State
from models.city import City
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from api.v1.views import states


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def all_cities(state_id=None):
    all_states = storage.all(State)
    sig = 0
    for key in all_states.keys():
        if state_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        all_cities = storage.all(City)
        list_of_dicts = []
        for values in all_cities.values():
            if state_id == values.state_id:
                list_of_dicts.append(BaseModel.to_dict(values))
        return jsonify(list_of_dicts)
    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        if 'name' not in json_dict.keys():
            abort(400, 'Missing name')
        else:
            new_city = City(**json_dict)
            new_city.save()
            return jsonify(BaseModel.to_dict(new_city)), 201


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
def cities_by_id(city_id=None):
    all_cities = storage.all(City)
    sig = 0
    for key in all_cities.keys():
        if city_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        return jsonify(BaseModel.to_dict(all_cities[key]))

    elif request.method == "DELETE":
        all_cities[key].delete()
        storage.save()
        return jsonify({}), 200

    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        for k, v in json_dict.items():
            if (k == 'id' or k == 'state_id' or
                    k == 'created_at' or k == 'updated_at'):
                continue
            else:
                setattr(all_cities[key], k, v)
        all_cities[key].save()
        return jsonify(BaseModel.to_dict(all_cities[key])), 200
