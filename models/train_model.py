import pandas as pd
import joblib
import os
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from utils.data_utils import load_configured_data
from utils import logger, config

def train():
    print("Reading the configuration file...📄")

    print("Loading the data...📊")
    df = load_configured_data(config)
    print("Data loaded successfully!✅")
    print("Data shape:", df.shape)
    print("Data columns:", df.columns.tolist())
    
    X = df[config.input_fields].fillna("").agg(" ".join, axis=1)
    y = df[config.output_fields].fillna("")

    print("Encoding output labels...🔡")
    encoders = {}
    y_encoded = pd.DataFrame()

    for col in config.output_fields:
        le = LabelEncoder()
        y_encoded[col] = le.fit_transform(y[col])
        encoders[col] = le

    print("Vectorizing input text...🔠")
    vectorizer = TfidfVectorizer(max_features=config.max_features)
    X_vec = vectorizer.fit_transform(X)

    print("Training the model...🧠")
    model = MultiOutputClassifier(RandomForestClassifier())
    model.fit(X_vec, y_encoded)
    print("Model trained successfully!✅")
    print("Model score: ", model.score(X_vec, y_encoded))
    model_dir = config.model_dir
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, "model.pkl"))
    joblib.dump(vectorizer, os.path.join(model_dir, "vectorizer.pkl"))
    joblib.dump(encoders, os.path.join(model_dir, "encoders.pkl"))

    logger.info("✅ Model, vectorizer, and encoders saved successfully.")

if __name__ == "__main__":
    train()
