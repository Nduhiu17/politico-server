"""user views comes here"""
from flask import Blueprint

auth_route = Blueprint('auth-v2', __name__, url_prefix='/api/v2/auth')