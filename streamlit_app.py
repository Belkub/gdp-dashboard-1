from PIL import Image
import streamlit as st

im = Image.open("C:\\west\\west_n.png")

steps = st.slider('Количество точек', 150, 600)

if st.button('Создать'):
    st.image("C:\\west\\west_n.png", caption="Sunrise by the mountains")
    ima = Image.open("C:\\west\\west_n.png")
    img = ima.crop((150, 150, 400, steps))  
    st.image(img)
