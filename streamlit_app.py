from PIL import Image
import streamlit as st
import plotly.express as px
im = Image.open("west_n.png")

steps = st.slider('Количество точек', 150, 600)

if st.button('Создать'):
    st.image("west_n.png", caption="Sunrise by the mountains")
    ima = Image.open("west_n.png")
    img = ima.crop((150, 150, 400, steps))  
    st.image(img)
if st.button('graph'):
    fig = px.scatter_3d(x=[1, 2, 3, 4], y=[4, 3, 2, 1], z=[1, 4, 2, 3])
    st.plotly_chart(fig)
