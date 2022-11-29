import models

from flask import request, jsonify, Blueprint
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

goal = Blueprint('goals', 'goal')

@goal.route('/new', methods = ['POST'])
def new_goal():
    payload = request.get_json()
    new_goal = models.Goal.create(**payload)
    goal_dict = model_to_dict(new_goal)
    return jsonify(
        data = goal_dict,
        message = 'New goal created',
        status = 201
    ), 201

@goal.route('/<id>', methods = ["DELETE"])
def delete_goal():
    query = models.Goal.delete().where(models.Goal.id == id)
    query.execute()
    return jsonify(
        data = 'Goal successfully deleted',
        message = 'Goal successfully deleted',
        status = 200
    ), 200