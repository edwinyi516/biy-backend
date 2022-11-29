import models

from flask import request, jsonify, Blueprint
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

module = Blueprint('modules', 'module')

@module.route('/new', methods = ['POST'])
def new_module():
    payload = request.get_json()
    new_module = models.Module.create(**payload)
    print("NEW MODULE BEFORE DICT")
    print(new_module)
    module_dict = model_to_dict(new_module)
    print("NEW MODEL AFTER DICT")
    print(module_dict)
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

@module.route('/', methods = ['GET'])
def get_module():
    current_user_modules = [model_to_dict(module) for module in current_user.modules]
    return jsonify(
        data = current_user_modules,
        message = 'Success',
        status = 200
    ), 200