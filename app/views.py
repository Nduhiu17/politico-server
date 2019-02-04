"""views"""
from flask import make_response, jsonify, Blueprint, request, abort

from app.models import Party
from utils.input_validators import Validate

version1 = Blueprint('api-v1', __name__, url_prefix='/api/v1')


@version1.route('/parties', methods=['GET'])
def get():
    """End point to get all parties"""
    all_parties = Party.get_all()
    return make_response(jsonify({
        "status": 200,
        "data": all_parties
    }))


@version1.route('/parties', methods=['POST'])
def post():
    """End point to post a political party"""

    if not request.json or not 'name' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Party name is required"
        }), 400)

    if not request.json or not 'hqaddress' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "hqaddress is required"
        }), 400)
    if not request.json or not 'logoUrl' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "logoUrl is required"
        }), 400)
    data = request.get_json(force=True)
    if type(data['name']) == int or type(data['hqaddress']) == int or type(data['logoUrl']) == int:
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)

    if not Validate.validate_name(name=data["name"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Invalid username"
        }), 400)
    if not Validate.validate_name_length(name=data["name"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Name should be atleast 5 characters long"
        }), 400)
    if Party.get_party_by_name(data["name"]):
        return make_response(jsonify({
            "status": 409,
            "error": "Party already registered"
        }), 409)

    name = data["name"]
    hqaddress = data["hqaddress"]
    logoUrl = data["logoUrl"]
    new_party = Party(name=name, hqaddress=hqaddress, logoUrl=logoUrl)
    new_party.save()
    return make_response(jsonify({
        "status": 201,
        "data": new_party.json_dumps()
    }), 201)
