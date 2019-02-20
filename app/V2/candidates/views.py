from datetime import datetime

from flask import Blueprint, request, make_response, jsonify

from app.V2.candidates.models import Candindate
from app.V2.offices.models import Office
from utils.helpers import admin_required, party_exists
from utils.input_validators import Validate

candindate_v2 = Blueprint('candindate-v2', __name__, url_prefix='/api/v2')


@candindate_v2.route('/office/<int:id>/register', methods=['POST'])
@admin_required
def post(id):
    """End point to post a candidate"""

    data = request.get_json(force=True)
    if len(data) < 2:
        return make_response(jsonify({
            "status": 400,
            "error": "party and candidate ids are required"
        }), 400)

    if isinstance(data['party'], int) or isinstance(data['candidate'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)
    if not Office.get_office_by_id(id=id):
        return make_response(jsonify({
            "status": 404,
            "error": "Office not found"
        }), 404)

    if Candindate.find_candidate_using_id(id=data["candidate"]):
        return make_response(jsonify({
            "status": 409,
            "error": "Candindate already registered"
        }), 409)

    office = id
    party = data["party"]
    candidate = data["candidate"]

    if Validate.validate_empty_string(data["party"]) or Validate.validate_empty_string(data["candidate"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Empty strings are not allowed"
        }), 400)
    if not party_exists(party_id=data["party"]):
        return make_response(jsonify({
            "status": 404,
            "error": "No registered party with that id"
        }), 404)

    new_candidate = Candindate(id=None, office=id, party=party, candidate=candidate, date_created=datetime.now(),
                               date_modified=datetime.now())
    Candindate.make_politician(candidate_id=candidate)
    new_candidate.save(office, party, candidate, datetime.now(), datetime.now())

    return make_response(jsonify({
        "status": 201,
        "message":"Successfully created candidate",
        "data": [new_candidate.json_dumps()]
    }), 201)
