import json
import os
import pickle
import numpy as np

model = None
data_columns = []

def loadModel():
    global model
    global data_columns

    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(script_dir, 'price-prediction-agentic-ai', 'model')

    if model is None:
        model_path = os.path.join(model_dir, 'dwelling_model.pickle')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print("model loaded successfully")

    if len(data_columns) == 0:
        locations_path = os.path.join(model_dir, 'locations.json')
        with open(locations_path, 'r') as f:
            data = json.load(f)
            data_columns = data.get('data_columns', [])
        print("location loaded successfully")
def get_price(location, area, bedrooms, bathrooms):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = area  # total_sqft
    x[1] = bathrooms  # bath
    x[2] = bedrooms  # bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)