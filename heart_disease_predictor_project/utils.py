def validate_input(data):
    required_features = ['feature1', 'feature2', ..., 'featureN']
    for feature in required_features:
        if feature not in data:
            return False
    return True
