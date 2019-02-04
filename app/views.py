"""views"""
from flask import make_response, jsonify, Blueprint, request, abort

from app.models import Party

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

    data = request.get_json()

    name = data["name"]
    hqaddress = data["hqaddress"]
    logoUrl = data["logoUrl"]
    new_party = Party(name=name, hqaddress=hqaddress, logoUrl=logoUrl)
    new_party.save()
    return make_response(jsonify({
        "status": 201,
        "data": new_party.json_dumps()
    }), 201)
