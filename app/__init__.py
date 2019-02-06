"""initializing the application"""
from flask import Flask
from flask_cors import CORS

from app.V1.offices.views import V1
from app.V1.parties.views import version1
from config import DevelopmentConfig

app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(version1)
app.register_blueprint(V1)

