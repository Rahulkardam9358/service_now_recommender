from flask import Blueprint, request, jsonify
from utils import logger
from api.recommender import get_predictions


api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        result = get_predictions(data)
        return jsonify(result)
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return jsonify({"error": str(e)}), 500


@api_blueprint.route('/')
def hello():
    return "Hello from Flask!!!"
