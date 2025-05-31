from PIL import Image
import streamlit as st

im = Image.open("west_n.png")

steps = st.slider('Количество точек', 150, 600)

if st.button('Создать'):
    st.image("west_n.png", caption="Sunrise by the mountains")
    crop_rectangle = (150, 150, 400, steps)
    img = im.crop(crop_rectangle)

    img.show()

