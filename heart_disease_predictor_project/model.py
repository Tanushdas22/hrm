import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def train_model():
    data = pd.read_csv('preprocessed_data.csv')
    X = data.drop('target', axis=1)
    y = data['target']
    
    model = RandomForestClassifier()
    model.fit(X, y)
    
    joblib.dump(model, 'heart_disease_model.pkl')

def load_model():
    return joblib.load('heart_disease_model.pkl')
