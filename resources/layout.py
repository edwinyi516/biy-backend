import models

from flask import request, jsonify, Blueprint
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

layout = Blueprint('layouts', 'layout')

@layout.route('/new', methods = ['POST'])
def new_layout():
    payload = request.get_json()
    new_layout = models.Layout.create(user = current_user.id, layout_data = payload('layout'))
    layout_dict = model_to_dict(new_layout)
    return jsonify(
        data = layout_dict,
        message = 'New layout created',
        status = 201
    ), 201

@layout.route('/')
def get_user_layout():
    layout = models.Layout.get(models.Layout.user == current_user.id)
    print(layout)
    return jsonify(
        data = model_to_dict(layout),
        message = 'Success',
        status = 200
    ), 200