#!/usr/bin/python3
""" Retrieves a list of all State objects"""

from flask import Flask, Blueprint, render_template, request, url_for, redirect, abort, jsonify, json
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
            return jsonify(BaseModel.to_dict(new_state))       
