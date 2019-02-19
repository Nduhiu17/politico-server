"""party views"""
from datetime import datetime

from flask import Blueprint, make_response, jsonify, request
from flask_jwt_extended import jwt_required

from app.V2.parties.models import Party
from utils.helpers import admin_required
from utils.input_validators import Validate

base_v2 = Blueprint('base-v2', __name__, url_prefix='/api/v2')



@base_v2.route('/parties', methods=['GET'])
@jwt_required
def get():
    """End point to get all parties"""
    all_parties = Party.get_all_parties()
    return make_response(jsonify({
        "status": 200,
        "data": all_parties
    }), 200)


@base_v2.route('/parties', methods=['POST'])
@jwt_required
@admin_required
def post():
    """End point to post a political party"""
    data = request.get_json(force=True)
    if len(data) < 4:
        return make_response(jsonify({
            "status": 400,
            "error": "name,hqaddress,logoUrl and slogan are required"
        }), 400)

    if isinstance(data['name'], int) or isinstance(data['hqaddress'], int) or isinstance(data['logoUrl'],
                                                                                         int) or isinstance(
            data['slogan'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)

    if Party.get_party_by_name(name=data["name"]):
        return make_response(jsonify({
            "status": 409,
            "error": "Party already registered"
        }), 409)

    name = data["name"]
    hqaddress = data["hqaddress"]
    logoUrl = data["logoUrl"]
    slogan = data["slogan"]

    if Validate.validate_empty_string(name) or Validate.validate_empty_string(
            hqaddress) or Validate.validate_empty_string(logoUrl) or Validate.validate_empty_string(slogan):
        return make_response(jsonify({
            "status": 400,
            "error": "Empty strings are not allowed"
        }), 400)

    new_party = Party(id=None, name=name, hqaddress=hqaddress, logoUrl=logoUrl, slogan=slogan,
                      date_created=datetime.now(),
                      date_modified=datetime.now())
    new_party.save(name, hqaddress, logoUrl, slogan, datetime.now(), datetime.now())
    party_saved = Party.get_party_by_name(name=name)

    return make_response(jsonify({
        "status": 201,
        "data": party_saved
    }), 201)


@base_v2.route('/parties/<int:id>', methods=['GET'])
@jwt_required
def get_a_party(id):
    """End point to get party by id"""
    party = Party.retrieve_by_id(id=id)
    if not party:
        return make_response(jsonify({
            "status": 404,
            "error": "No party with that id"
        }), 404)

    return make_response(jsonify({
        "status": 200,
        "data": party
    }), 200)
