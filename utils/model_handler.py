# model_handler.py

import cv2
from keras.models import load_model
from utils.model_predict import make_prediction

def load_keras_model(model_path):
    return load_model(model_path)

def handle_model_prediction(file_path, model):
    try:
        predicted_label = make_prediction(file_path, model)
        print(f"Testing model with image: {file_path}")
        return predicted_label
    except Exception as e:
        print(f"Error testing model with image {file_path}: {str(e)}")
        return f'Error testing model: {str(e)}'