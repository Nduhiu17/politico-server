"""user views comes here"""
from datetime import datetime

from flask import Blueprint, request, make_response, jsonify

from app.V2.auth.models import User
from utils.input_validators import Validate

auth_route = Blueprint('auth-v2', __name__, url_prefix='/api/v2/auth')


@auth_route.route('/signup', methods=['POST'])
def post():
    """End point to post a political party"""
    data = request.get_json(force=True)
    if len(data) < 9:
        return make_response(jsonify({
            "status": 400,
            "error": "firstname,lastname,othername,email,phonenumber,passporturl and password are required"
        }), 400)

    data = request.get_json(force=True)

    if isinstance(data['firstname'], int) or isinstance(data['lastname'], int) or isinstance(data['email'],
                                                                                             int) or isinstance(
        data['phonenumber'], int) or isinstance(data['passporturl'], int) or isinstance(data['password'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)

    if not Validate.validate_email_format(email=data["email"]) or Validate.check_email_int(email=data["email"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Invalid email.The email should be of type 'example@mail.com'"
        }), 400)

    if User.get_by_email(email=data['email']):
        return make_response(jsonify({
            "status": 409,
            "error": "Email already taken"
        }), 409)
    if User.find_by_nationaid(id=data['nationalid']):
        return make_response(jsonify({
            "status": 409,
            "error": "A voter with that national id already exists"
        }), 409)

    firstname = data["firstname"]
    lastname = data["lastname"]
    othername = data["othername"]
    email = data["email"]
    phonenumber = data["phonenumber"]
    passporturl = data["passporturl"]
    nationalid = data["nationalid"]
    county = data["county"]
    password = data["password"]
    if Validate.validate_empty_string(firstname) or Validate.validate_empty_string(
            lastname) or Validate.validate_empty_string(othername) or Validate.validate_empty_string(
        email) or Validate.validate_empty_string(phonenumber) or Validate.validate_empty_string(
        passporturl) or Validate.validate_empty_string(password):
        return make_response(jsonify({
            "status": 400,
            "error": "Empty strings are not allowed"
        }), 400)

    if not Validate.check_number_format(input_value=nationalid):
        return make_response(jsonify({
            "status": 400,
            "error": "National id must be an integer"
        }), 400)
    if not Validate.check_phone_number(phone_number=phonenumber):
        return make_response(jsonify({
            "status": 400,
            "error": "Invalid phone number.The phone number should be of type '0722117264'"
        }), 400)
    if not Validate.check_password_strength(input_password=password):
        return make_response(jsonify({
            "status": 400,
            "error": "Weak password,the password should contain a symbol,capital letter and 8 digits long"
        }), 400)

    new_user = User(id=None, firstname=firstname, lastname=lastname, othername=othername, email=email,
                    phonenumber=phonenumber, passporturl=passporturl, roles="voter", nationalid=nationalid,
                    county=county,
                    password=User.generate_hash(password=password), date_created=datetime.now(),
                    date_modified=datetime.now())
    new_user.save(firstname, lastname, othername, email, phonenumber, passporturl, "voter", nationalid, county,
                  User.generate_hash(password=password), datetime.now(), datetime.now())

    access_token = User.generate_token(email=data["email"])

    return make_response(jsonify({
        "status": 201,
        "user": new_user.json_dump(),
        "token": access_token,
        "message": "User registered"
    }), 201)


@auth_route.route('/login', methods=['POST'])
def login():
    """End point to login a user"""

    data = request.get_json(force=True)

    if len(data) < 2:
        return make_response(jsonify({
            "status": 400,
            "error": "Both email and password are required"
        }), 400)

    if isinstance(data['email'], int) or isinstance(data['password'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)

    if Validate.validate_empty_string(data['email']) or Validate.validate_empty_string(data['password']):
        return make_response(jsonify({
            "status": 400,
            "error": "Empty strings are not allowed"
        }), 400)

    if not Validate.validate_email_format(email=data["email"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Invalid email.The email should be of type 'example@mail.com'"
        }), 400)

    current_user = User.get_by_email(data['email'])
    if not current_user:
        return make_response(jsonify({
            "status": 404,
            "error": "User not yet registered"
        }), 404)

    if not User.verify_hashed_password(data['password'], current_user[10]):
        return make_response(jsonify({
            "status": 403,
            "error": "Wrong credentials"
        }), 403)
    access_token = User.generate_token(email=data["email"])
    logged_user = User(id=current_user[0], firstname=current_user[1], lastname=current_user[2],
                       othername=current_user[3], email=current_user[4], phonenumber=current_user[5],
                       passporturl=current_user[6], roles=current_user[7], nationalid=current_user[8],
                       county=current_user[9], password=current_user[10], date_created=current_user[11],
                       date_modified=current_user[12])
    return make_response(jsonify({
        "status": 200,
        "data": logged_user.json_dump(),
        "access_token": access_token,
        "message": "logged in"
    }), 200)
