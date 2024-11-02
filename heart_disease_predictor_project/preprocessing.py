import numpy as np

def preprocess_input(data):
    processed_data = np.array([data['feature1'], data['feature2'], ..., data['featureN']])
    return processed_data.reshape(1, -1)
