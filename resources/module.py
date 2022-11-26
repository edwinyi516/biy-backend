import models

from flask import request, jsonify, Blueprint
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

module = Blueprint('modules', 'module')

@module.route('/new', methods = ['POST'])
def new_module():
    payload = request.get_json()
    new_module = models.Module.create(**payload)
    module_dict = model_to_dict(new_module)
    return jsonify(
        data = module_dict,
        message = 'New module created',
        status = 201
    ), 201

@module.route('/delete', methods = ["DELETE"])
def delete_module():
    payload = request.get_json()
    query = models.Module.delete().where((models.User.id == current_user.id) and (models.Module.i_value == payload['i_value']))
    query.execute()
    return jsonify(
        data = 'Module deleted successfully',
        message = 'Module successfully deleted',
        status = 200
    ), 200

@module.route('/')
def get_module():
    payload = request.get_json()
    module = models.Module.get((models.Module.user == current_user.id) and (models.Module.i_value == payload['i_value']))
    print(module)
    return jsonify(
        data = model_to_dict(module),
        message = 'Success',
        status = 200
    ), 200