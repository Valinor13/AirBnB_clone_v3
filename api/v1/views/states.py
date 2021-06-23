#!/usr/bin/python3
""" Retrieves a list of all State objects"""

from flask import Flask, Blueprint, render_template
from flask import request, url_for, redirect, abort, jsonify, json
from models.state import State
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from console import HBNBCommand


@app_views.route('/states', methods=['GET', 'POST'])
def all_states():
    if request.method == "GET":
        all_states = storage.all(State)
        list_of_dicts = []
        for values in all_states.values():
            list_of_dicts.append(BaseModel.to_dict(values))
        return jsonify(list_of_dicts)
    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        if 'name' not in json_dict.keys():
            abort(400, 'Missing name')
        else:
            new_state = State(name=json_dict['name'])
            new_state.save()
            return jsonify(BaseModel.to_dict(new_state)), 201


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def states_by_id(state_id=None):
    all_states = storage.all(State)
    sig = 0
    for key in all_states.keys():
        if state_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        return jsonify(BaseModel.to_dict(all_states[key]))

    elif request.method == "DELETE":
        all_states[key].delete()
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
                setattr(all_states[key], k, v)
        all_states[key].save()
        return jsonify(BaseModel.to_dict(all_states[key])), 200
