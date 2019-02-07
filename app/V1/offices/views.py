"""views"""
from flask import make_response, jsonify, Blueprint, request

from app.V1.offices.models import Office

from utils.input_validators import Validate

V1 = Blueprint('api-version1', __name__, url_prefix='/api/v1')


@V1.route('/offices', methods=['POST'])
def post():
    """End point to post a political party"""

    if not request.json or not 'name' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Office name is required"
        }), 400)

    if not request.json or not 'office_type' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Office type is required"
        }), 400)

    data = request.get_json(force=True)
    if isinstance(data['name'], int) or isinstance(data['office_type'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)

    if not Validate.validate_name(name=data["name"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Invalid name"
        }), 400)
    if not Validate.validate_name_length(name=data["name"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Name should be atleast 5 characters long"
        }), 400)
    if Office.get_office_by_name(name=data["name"]):
        return make_response(jsonify({
            "status": 409,
            "error": "Office already registered"
        }), 409)
    name = data["name"]
    office_type = data["office_type"]
    new_office = Office(office_type=office_type, name=name)
    new_office.save()
    return make_response(jsonify({
        "status": 201,
        "data": new_office.json_dumps()
    }), 201)


@V1.route('/offices', methods=['GET'])
def get():
    """End point to get all offices"""
    all_offices = Office.get_all_offices()
    return make_response(jsonify({
        "status": 200,
        "data": all_offices
    }), 200)


@V1.route('/offices/<int:id>', methods=['GET'])
def get_an_office(id):
    """End point to get an office by id"""
    retrieved_office = Office.get_office_by_id(id=id)
    if retrieved_office:
        return make_response(jsonify({
            "status": 200,
            "data": retrieved_office
        }))
    return make_response(jsonify({
        "status": 404,
        "data": "No office found with that id"
    }), 404)
