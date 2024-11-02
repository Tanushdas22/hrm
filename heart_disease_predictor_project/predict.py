from model import load_model
from preprocessing import preprocess_input

model = load_model()

def make_prediction(data):
    processed_data = preprocess_input(data)
    prediction = model.predict(processed_data)
    return prediction[0]
