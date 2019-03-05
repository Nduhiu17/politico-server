"""application views"""
from datetime import datetime

from flask import Blueprint, make_response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.V2.applications.models import Application
from app.V2.auth.models import User
from app.V2.offices.models import Office
from app.V2.parties.models import Party
from utils.input_validators import Validate

application_v2 = Blueprint('application-v2', __name__, url_prefix='/api/v2')


@application_v2.route('/applications', methods=['POST'])
@jwt_required
def post():
    """End point to post an application"""

    data = request.get_json(force=True)
    if len(data) < 2:
        return make_response(jsonify({
            "status": 400,
            "error": "office and party names are required"
        }), 400)

    if isinstance(data['party_name'], int) or isinstance(data['office_name'], int):
        return make_response(jsonify({
            "status": 400,
            "error": "Post data of type strings"
        }), 400)
    if Validate.validate_empty_string(data["party_name"]) or Validate.validate_empty_string(data["office_name"]):
        return make_response(jsonify({
            "status": 400,
            "error": "Empty strings are not allowed"
        }), 400)
    if not Party.get_party_by_name(name=data["party_name"]):
        return make_response(jsonify({
            "status": 404,
            "error": "Party not yet registered"
        }), 404)
    if not Office.get_office_by_name(data["office_name"]):
        return make_response(jsonify({
            "status": 404,
            "error": "Office not yet registered"
        }), 404)

    party_name = data["party_name"]
    office_name = data["office_name"]
    user_id = User.get_by_email(email=get_jwt_identity())[0]
    if Application.get_application_by_user_id(user_id=user_id):
        return make_response(jsonify({
            "status": 409,
            "error": "You have already submitted your application"
        }), 409)

    new_application = Application(id=None,party_name=party_name,office_name=office_name,user_id=user_id,date_created=datetime.now())
    new_application.save(party_name,office_name,user_id,datetime.now())

    return make_response(jsonify({
        "status": 201,
        "data": new_application.json_dumps()
    }), 201)


