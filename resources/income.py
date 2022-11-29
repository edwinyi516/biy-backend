import models

from flask import request, jsonify, Blueprint
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

income = Blueprint('incomes', 'income')

@income.route('/new', methods = ['POST'])
def new_income():
    payload = request.get_json()
    new_income = models.Income.create(**payload)
    income_dict = model_to_dict(new_income)
    return jsonify(
        data = income_dict,
        message = 'New income created',
        status = 201
    ), 201

@income.route('/<id>', methods = ["DELETE"])
def delete_income():
    query = models.Income.delete().where(models.Income.id == id)
    query.execute()
    return jsonify(
        data = 'Income successfully deleted',
        message = 'Income successfully deleted',
        status = 200
    ), 200