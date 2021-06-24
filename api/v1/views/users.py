#!/usr/bin/python3
""" Retrieves a list of all State objects"""

from flask import Flask, Blueprint, render_template
from flask import request, url_for, redirect, abort, jsonify, json
from models.state import State
from models.user import User
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage


@app_views.route('/users', methods=['GET', 'POST'])
def all_users():
    if request.method == "GET":
        all_users = storage.all(User)
        list_of_dicts = []
        for values in all_users.values():
            list_of_dicts.append(BaseModel.to_dict(values))
        return jsonify(list_of_dicts)
    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        if 'email' not in json_dict.keys():
            abort(400, 'Missing email')
        elif 'password' not in json_dict.keys():
            abort(400, 'Missing password')
        else:
            new_users = User(first_name=json_dict['first_name'],
                             last_name=json_dict['last_name'],
                             email=json_dict['email'],
                             password=json_dict['password'])
            new_users.save()
            return jsonify(BaseModel.to_dict(new_users)), 201


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'])
def user_by_id(user_id=None):
    all_users = storage.all(User)
    sig = 0
    for key in all_users.keys():
        if user_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        return jsonify(BaseModel.to_dict(all_users[key]))

    elif request.method == "DELETE":
        all_users[key].delete()
        storage.save()
        return jsonify({}), 200

    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        for k, v in json_dict.items():
            if (k == 'id' or k == 'created_at' or
                    k == 'updated_at' or k == 'email'):
                continue
            else:
                setattr(all_users[key], k, v)
        all_users[key].save()
        return jsonify(BaseModel.to_dict(all_users[key])), 200
