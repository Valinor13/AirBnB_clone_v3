#!/usr/bin/python3
""" Retrieves a list of all City objects"""

from flask import Flask, Blueprint, render_template
from flask import request, url_for, redirect, abort, jsonify, json
from models.city import City
from models.user import User
from models.place import Place 
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from api.v1.views import states


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'])
def all_places(city_id=None):
    all_cities = storage.all(City)
    sig = 0
    for key in all_cities.keys():
        if city_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        all_places = storage.all(Place)
        list_of_dicts = []
        for values in all_places.values():
            if city_id == values.city_id:
                list_of_dicts.append(BaseModel.to_dict(values))
        return jsonify(list_of_dicts)
    else:
        sig = 0
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        if 'name' not in json_dict.keys():
            abort(400, 'Missing name')
        if 'user_id' not in json_dict.keys():
            abort(400, 'Missing user_id')
        for user in storage.all(User).values():
            if json_dict['user_id'] == user.id:
                sig = 1
                break
        if sig == 0:
            abort(404)
        else:
            new_place= Place(**json_dict)   
            new_place.save()
            return jsonify(BaseModel.to_dict(new_place)), 201


@app_views.route('/places/<place_id>', methods=['GET', 'DELETE', 'PUT'])
def place_by_id(place_id=None):
    all_places = storage.all(Place)
    sig = 0
    for key in all_places.keys():
        if place_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        return jsonify(BaseModel.to_dict(all_places[key]))

    elif request.method == "DELETE":
        all_places[key].delete()
        storage.save()
        return jsonify({}), 200

    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        for k, v in json_dict.items():
            if (k == 'id' or k == 'city_id' or k == 'user_id'
                    k == 'created_at' or k == 'updated_at'):
                continue
            else:
                setattr(all_places[key], k, v)
        all_places[key].save()
        return jsonify(BaseModel.to_dict(all_places[key])), 200
