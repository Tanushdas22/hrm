from flask import Flask, request, jsonify
from predict import make_prediction
from utils import validate_input
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not validate_input(data):
        return jsonify({'error': 'Invalid input'}), 400
    result = make_prediction(data)
    return jsonify({'prediction': int(result)})

if __name__ == '__main__':
    app.run(debug=True)
