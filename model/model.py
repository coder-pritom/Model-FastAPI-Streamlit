import pickle
import pandas as pd

with open('model/trained_model.pkl','rb') as file:
    model = pickle.load(file)

def prediction(input):
    input = pd.DataFrame([input])
    pred = model.predict(input)[0]
    return pred