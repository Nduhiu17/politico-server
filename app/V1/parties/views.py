"""views"""
from flask import make_response, jsonify, Blueprint, request

from app.V1.parties.models import Party

from utils.input_validators import Validate

version1 = Blueprint('api-v1', __name__, url_prefix='/api/v1')


@version1.route('/parties', methods=['GET'])
def get():
    """End point to get all parties"""
    all_parties = Party.get_all()
    return make_response(jsonify({
        "status": 200,
        "data": all_parties
    }), 200)


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
    if isinstance(data['name'], int) or isinstance(data['hqaddress'], int) or isinstance(data['logoUrl'], int) == int:
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


@version1.route('/parties/<int:id>', methods=['GET'])
def get_a_party(id):
    """End point to get a party by id"""
    party_retrieved = Party.get_party_by_id(id=id)
    if party_retrieved:
        return make_response(jsonify({
            "status": 200,
            "data": party_retrieved
        }))
    return make_response(jsonify({
        "status": 404,
        "data": "No party found with that id"
    }), 404)


@version1.route('/parties/<int:id>/name', methods=['PATCH'])
def patch(id):
    """End point to modify a party"""

    if not request.json or not 'name' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "Party name is required"
        }), 400)

    data = request.get_json(force=True)
    if isinstance(data['name'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Name should be of type strings"
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
            "error": "Party name already taken"
        }), 409)

    name = data["name"]
    party_to_edit = Party.get_party_by_id(id=id)
    new_party = Party(name=name, hqaddress=party_to_edit[0]['hqaddress'], logoUrl=party_to_edit[0]['logoUrl'])
    new_party.update_party(id=None, name=name, hqaddress=party_to_edit[0]['hqaddress'],
                           logoUrl=party_to_edit[0]['logoUrl'])
    return make_response(jsonify({
        "status": 201,
        "data": new_party.json_dumps()
    }), 201)


@version1.route('/parties/<int:id>', methods=['DELETE'])
def delete(id):
    """End point to delete a party"""
    party_to_delete = Party.get_party_by_id(id=id)
    if party_to_delete:
        Party.delete_party(id=id)
        return make_response(jsonify({
            "status": 204,
            "message": "deleted"
        }))
    return make_response(jsonify({
        "status": 404,
        "error": "No party found with that id"
    }), 404)
