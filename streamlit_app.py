import os
import json 
import streamlit as st
import time 
import joblib
import sklearn 
from sklearn.linear_model import LogisticRegression
import pickle

from PIL import Image


model = joblib.load('clf.joblib')
st.title('С кем сходство из голливудских актрис?')

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

def change_photo_state():
    st.session_state["photo"]="done"

uploaded_photo = st.file_uploader("Загрузите фотографию", on_change=change_photo_state)

if st.session_state["photo"]=="done":
    progress_bar = st.progress(0)

    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)

    st.success('Фото успешно загружено')    

def resize_image(SIZE, image):
    # получим его размер
    size = image.size
    print("size = ", size)
    # получим коэффициент, на который нужно уменьшить/увеличить
    # изображение по одной из сторон до 256
    coef = SIZE / size[0]
    # изменяем размер изображения
    resized_image = image.resize(
        (int(size[0] * coef), int(size[1] * coef)))
    res_image = resized_image.convert('RGB')
    return res_image

SIZE = 1024

res_image = resize_image(SIZE, uploaded_photo)

def predict():
    prediction = model.predict(res_image)

trigger = st.button('Показать', on_click=predict)        
