"""party views"""
from flask import Blueprint, make_response, jsonify
from flask_jwt_extended import jwt_required

from app.V2.parties.models import Party

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
