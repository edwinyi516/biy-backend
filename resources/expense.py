import models

from flask import request, jsonify, Blueprint
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

expense = Blueprint('expenses', 'expense')

@expense.route('/new', methods = ['POST'])
def new_expense():
    payload = request.get_json()
    new_expense = models.Expense.create(**payload)
    expense_dict = model_to_dict(new_expense)
    return jsonify(
        data = expense_dict,
        message = 'New expense created',
        status = 201
    ), 201

@expense.route('/<id>', methods = ["DELETE"])
def delete_expense():
    query = models.Expense.delete().where(models.Expense.id == id)
    query.execute()
    return jsonify(
        data = 'Expense successfully deleted',
        message = 'Expense successfully deleted',
        status = 200
    ), 200