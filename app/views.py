from flask import make_response, jsonify, Blueprint

from app.models import Party

version1 = Blueprint('api-v1', __name__, url_prefix='/api/v1')


@version1.route('/parties', methods=['GET'])
def get():
    """End point to get all parties"""
    all_parties = Party.get_all()
    return make_response(jsonify({
        "status": '200 OK',
        "data": all_parties
    }))
