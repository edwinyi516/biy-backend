import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user')

@user.route('/signup', methods = ["POST"])
def signup():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    try:
        #find if user already exists
        models.User.get(models.User.email == payload['email'])
        return jsonify(data = {}, status = {"code": 401, "message": "User already exists"}), 401
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        user = models.User.create(**payload)
        user_dict = model_to_dict(user)
        print(user_dict)
        print(type(user_dict))
        del user_dict['password']
        return jsonify(data = user_dict, status = {"code": 201, "message": "Success"}), 201

@user.route('/login', methods = ["POST"])
def login():
    payload = request.get_json()
    remember_checked = payload['remember']
    print(remember_checked)
    try:
        user = models.User.get(models.User.email == payload['email'].lower())
        user_dict = model_to_dict(user)
        if (check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user, remember = remember_checked)
            print(user, "Logging in this user")
            return jsonify(data = user_dict, status = {"code": 200, "message": "Success"}), 200
        else:
            return jsonify(data = {}, status = {"code": 401, "message": "Email or password is incorrect"}), 401
    except models.DoesNotExist:
        return jsonify(data = {}, status = {"code": 401, "message": "Email or password is incorrect"}), 401

@user.route('/logout', methods = ["GET"])
def logout():
    logout_user()
    return jsonify(data = {}, status = 200, message = "Logout successful"), 200

#Logged in user route
@user.route('/currentuser', methods = ["GET"])
def getloggedinuser():
    print(current_user)
    print(type(current_user))
    if current_user:
        user_dict = model_to_dict(current_user)
        user_dict.pop('password')
        return jsonify(data = user_dict), 200
    else:
        return jsonify(data = {}, status = 401, message = "No user is logged in"), 401