import os
import json
import joblib
from utils import logger, config

from sklearn.feature_extraction.text import TfidfVectorizer

from utils.response_utils import reframe_output

model_dir = config.model_dir

# Load model, vectorizer, and encoders
model = joblib.load(os.path.join(model_dir, "model.pkl"))
vectorizer: TfidfVectorizer = joblib.load(os.path.join(model_dir, "vectorizer.pkl"))
encoders = joblib.load(os.path.join(model_dir, "encoders.pkl"))


def get_predictions(data: dict):
    """
    Given a dictionary with input_fields, predict output_fields.
    """
    try:
        # Merge all input fields into one text string
        input_text = " ".join([data.get(field, "") for field in config.input_fields])
        logger.info(f"Input for prediction: {input_text}")

        # Vectorize input text
        X_vec = vectorizer.transform([input_text])

        # Predict encoded labels
        encoded_preds = model.predict(X_vec)[0]

        # Decode predictions using saved encoders
        decoded_output = {
            field: encoders[field].inverse_transform([pred])[0]
            for field, pred in zip(config.output_fields, encoded_preds)
        }

        # Reframe and return the response
        final_response = reframe_output(decoded_output)
        logger.info(f"Prediction result: {final_response}")
        return final_response

    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return {"error": "Prediction failed", "details": str(e)}
