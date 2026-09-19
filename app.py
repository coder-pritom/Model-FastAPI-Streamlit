from fastapi import FastAPI
from schema.user_input import Student
from database.data import load_data,save_data
from model.model import model,prediction
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
def home():
    return "Porasuna Valo Na! Biye Korbo 😁"

@app.post("/predict")
def predict_result(student: Student):
    new_data = student.model_dump()
    features = student.model_dump(include=['study_hours','playing_hours'])
    
    pred = prediction(features)
    new_data['result'] = 'Pass' if pred == 1 else 'Fail'

    data = load_data()
    if data == {}:
        first_data = {"0":new_data}
        save_data(first_data)
    else:
        data[str(int(list(data.keys())[-1])+1)] = new_data
        save_data(data)

    return JSONResponse(status_code=200, content={"result":new_data['result']})