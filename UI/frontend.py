import streamlit as st
import requests
from fastapi import HTTPException

api_link = "http://127.0.0.1:8000/predict"

st.title("Student Result",text_alignment='center')

name = st.text_input(label='Enter Name')
cls = st.number_input(label='Enter Class',value=None,)
study = st.number_input(label='Enter Study Hours')
play = st.number_input(label='Enter Playning Hours')

button = st.button(label='Result')

if button:
    data = {
        "name": name,
        "cls" : int(cls),
        "study_hours" : study,
        "playing_hours" : play
    }

    try:
        response = requests.post(api_link,json=data)
        if response.status_code == 200:
            result = response.json()
            st.markdown(f'Your Result: {result['result']}')
        else:
            raise HTTPException(404,"Request not done!")
    except:
        raise requests.exceptions.ConnectionError
