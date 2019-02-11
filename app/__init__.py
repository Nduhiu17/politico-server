"""initializing the application"""
from flask import Flask, render_template, jsonify
from flask_cors import CORS

from app.V1.offices.views import V1
from app.V1.parties.views import version1
from config import DevelopmentConfig

app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(version1)
app.register_blueprint(V1)


@app.errorhandler(405)
def handle_405_error(e):
    return jsonify({
        "status": 405,
        "message": "method not allowed"
    }), 405


@app.errorhandler(404)
def handle_404_error(e):
    return jsonify({
        "status": 404,
        "message": "Not found"
    }), 404


@app.errorhandler(503)
def handle_503_error(e):
    return jsonify({
        "status": 503,
        "message": "Service unavailable"
    })


@app.errorhandler(400)
def handle_400_error(e):
    return jsonify({
        "status": 400,
        "message": "Bad request.Please try again"
    }), 400


@app.errorhandler(408)
def handle_408_error(e):
    return jsonify({
        "status": 408,
        "message": "Request time out"
    }), 408


@app.errorhandler(429)
def handle_429_error(e):
    return jsonify({
        "status": 429,
        "message": "Too Many Requests"
    }), 429


@app.route("/")
def index():
    return render_template("docs.html")
