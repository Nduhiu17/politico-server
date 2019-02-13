"""user views comes here"""
from datetime import datetime

from flask import Blueprint, request, make_response, jsonify

from app.V2.auth.models import User
from utils.input_validators import Validate

auth_route = Blueprint('auth-v2', __name__, url_prefix='/api/v2/auth')


@auth_route.route('/signup', methods=['POST'])
def post():
    """End point to post a political party"""

    if not request.json or not 'firstname' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "First name is required"
        }), 400)

    if not request.json or not 'lastname' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Last name is required"
        }), 400)
    if not request.json or not 'othername' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "othername is required"
        }), 400)
    if not request.json or not 'email' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Email is required"
        }), 400)
    if not request.json or not 'phonenumber' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Phone number is required"
        }), 400)
    if not request.json or not 'passporturl' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Passporturl is required"
        }), 400)

    if not request.json or not 'password' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Password is required"
        }), 400)

    data = request.get_json(force=True)

    if isinstance(data['firstname'], int) or isinstance(data['lastname'], int) or isinstance(data['email'],
                                                                                             int) or isinstance(
        data['phonenumber'], int) or isinstance(data['passporturl'], int) or isinstance(data['password'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)

    if not Validate.validate_email_format(email=data["email"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Invalid email.The email should be of type 'example@mail.com'"
        }), 400)

    if User.get_by_email(email=data['email']):
        return make_response(jsonify({
            "status": 409,
            "error": "Email already taken"
        }), 409)

    firstname = data["firstname"]
    lastname = data["lastname"]
    othername = data["othername"]
    email = data["email"]
    phonenumber = data["phonenumber"]
    passporturl = data["passporturl"]
    password = data["password"]

    new_user = User(id=None, firstname=firstname, lastname=lastname, othername=othername, email=email,
                    phonenumber=phonenumber,
                    passporturl=passporturl, password=password, date_created=datetime.now(),
                    date_modified=datetime.now())
    new_user.save(firstname=firstname, lastname=lastname, othername=othername, email=email, phonenumber=phonenumber,
                  passporturl=passporturl, password=User.generate_hash(password=password))

    access_token = User.generate_token(email=data["email"])

    return make_response(jsonify({
        "status": 201,
        "user": new_user.json_dump(),
        "token": access_token,
        "message": "User registered"
    }), 201)
