from datetime import datetime

from flask import make_response, jsonify, Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.V2.auth.models import User
from app.V2.offices.models import Office
from app.V2.votes.models import Vote
from utils.input_validators import Validate

votes_base = Blueprint('votes-base', __name__, url_prefix='/api/v2')


@votes_base.route('/votes', methods=['POST'])
@jwt_required
def post():
    """End point to vote"""
    data = request.get_json(force=True)
    if len(data) < 2:
        return make_response(jsonify({
            "status": 400,
            "error": "office and candidate are required"
        }), 400)

    if not isinstance(data['office'], str) or not isinstance(data['candidate'], str):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)

    office = data["office"]
    candidate = data["candidate"]

    if Validate.validate_empty_string(office) or Validate.validate_empty_string(candidate):
        return make_response(jsonify({
            "status": 400,
            "error": "Empty strings are not allowed"
        }), 400)
    createdBy = User.get_by_email(email=get_jwt_identity())[0]
    user_candidate_county = User.find_user_by_id(id=int(candidate))['county']
    voter_county = User.get_by_email(email=get_jwt_identity())[9]
    office_to_vote = Office.get_office_by_id(id=int(office))['name']
    if office_to_vote != "president":
        if user_candidate_county != voter_county:
            return make_response(jsonify({
                "status": 400,
                "error": "You are only allowed to vote where you registered"
            }), 400)
    if Vote.check_already_voted(createdBy=createdBy):
        return make_response(jsonify({
            "status": 409,
            "error": "You already voted"
        }), 409)
    new_vote = Vote(id=None, candidate=candidate, createdOn=datetime.now(), createdBy=createdBy, office=office)
    new_vote.save(datetime.now(), createdBy, office, candidate)

    return make_response(jsonify({
        "message":"voted successfully",
        "status": 201,
        "data": {
            "office": int(office),
            "candidate": int(candidate),
            "voter": createdBy
        }
    }), 201)
