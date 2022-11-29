import models

from flask import request, jsonify, Blueprint
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

bill = Blueprint('bills', 'bill')

@bill.route('/new', methods = ['POST'])
def new_bill():
    payload = request.get_json()
    new_bill = models.Bill.create(**payload)
    bill_dict = model_to_dict(new_bill)
    return jsonify(
        data = bill_dict,
        message = 'New bill created',
        status = 201
    ), 201

@bill.route('/<id>', methods = ["DELETE"])
def delete_bill():
    query = models.Bill.delete().where(models.Bill.id == id)
    query.execute()
    return jsonify(
        data = 'Bill successfully deleted',
        message = 'Bill successfully deleted',
        status = 200
    ), 200