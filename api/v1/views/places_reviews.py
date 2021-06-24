#!/usr/bin/python3
""" Retrieves a list of all City objects"""

from flask import Flask, Blueprint, render_template
from flask import request, url_for, redirect, abort, jsonify, json
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from api.v1.views import states


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
def all_reviews(place_id=None):
    all_places = storage.all(Place)
    sig = 0
    for key in all_places.keys():
        if place_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        all_reviews = storage.all(Review)
        list_of_dicts = []
        for values in all_reviews.values():
            if place_id == values.place_id:
                list_of_dicts.append(BaseModel.to_dict(values))
        return jsonify(list_of_dicts)
    else:
        sig = 0
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        if 'user_id' not in json_dict.keys():
            abort(400, 'Missing user_id')
        if 'text' not in json_dict.keys():
            abort(400, 'Missing text')
        for user in storage.all(User).values():
            if json_dict['user_id'] == user.id:
                sig = 1
                break
        if sig == 0:
            abort(404)
        else:
            json_dict['place_id'] = place_id
            new_review = Review(**json_dict)
            new_review.save()
            return jsonify(BaseModel.to_dict(new_review)), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'])
def review_by_id(review_id=None):
    all_reviews = storage.all(Review)
    sig = 0
    for key in all_reviews.keys():
        if review_id in key:
            sig = 1
            break
    if sig == 0:
        abort(404)
    if request.method == "GET":
        return jsonify(BaseModel.to_dict(all_reviews[key]))

    elif request.method == "DELETE":
        all_reviews[key].delete()
        storage.save()
        return jsonify({}), 200

    else:
        json_dict = request.get_json()
        if not json_dict:
            abort(400, 'Not a JSON')
        for k, v in json_dict.items():
            if (k == 'id' or k == 'place_id' or k == 'user_id' or
                    k == 'created_at' or k == 'updated_at'):
                continue
            else:
                setattr(all_reviews[key], k, v)
        all_reviews[key].save()
        return jsonify(BaseModel.to_dict(all_reviews[key])), 200
