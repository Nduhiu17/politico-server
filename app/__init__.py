"""initializing the application"""
from flask import Flask
from flask_cors import CORS

from app.views import version1, V1
from config import DevelopmentConfig

app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(version1)
app.register_blueprint(V1)

from . import views, models
