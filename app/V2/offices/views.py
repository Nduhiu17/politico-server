"""office views"""
from datetime import datetime

from flask import Blueprint, make_response, request, jsonify
from flask_jwt_extended import jwt_required

from app.V2.offices.models import Office
from utils.helpers import offices_allowed, office_names_allowed, admin_required
from utils.input_validators import Validate

office_v2 = Blueprint('office-v2', __name__, url_prefix='/api/v2')


@office_v2.route('/offices', methods=['POST'])
@jwt_required
@admin_required
def post():
    """End point to post a political party"""

    data = request.get_json(force=True)
    if len(data) < 2:
        return make_response(jsonify({
            "status": 400,
            "error": "name and office type are required"
        }), 400)

    if isinstance(data['name'], int) or isinstance(data['office_type'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)

    office_type = data["office_type"]
    if office_type not in offices_allowed:
        return make_response(jsonify({
            "status": 400,
            "error": "That office type is not allowed"
        }), 400)
    office_type = data["name"]
    if office_type not in office_names_allowed:
        return make_response(jsonify({
            "status": 400,
            "error": "That office name is not yet allowed"
        }), 400)
    if Office.get_office_by_name(data["name"]):
        return make_response(jsonify({
            "status": 409,
            "error": "Office name already registered"
        }), 409)

    name = data["name"]
    office_type = data["office_type"]

    if Validate.validate_empty_string(name) or Validate.validate_empty_string(office_type):
        return make_response(jsonify({
            "status": 400,
            "error": "Empty strings are not allowed"
        }), 400)

    new_office = Office(id=None, name=name, office_type=office_type, date_created=datetime.now(),
                        date_modified=datetime.now())
    new_office.save(name, office_type, datetime.now(), datetime.now())

    return make_response(jsonify({
        "status": 201,
        "data": new_office.json_dumps()
    }), 201)


@office_v2.route('/offices', methods=['GET'])
@jwt_required
def get():
    """End point to get all offices"""
    all_offices = Office.get_all_offices()
    return make_response(jsonify({
        "status": 200,
        "data": all_offices
    }), 200)
