from flask import Flask
from api.routes import api_blueprint
from utils import logger

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)

    logger.info("Flask app initialized.")
    
    return app
