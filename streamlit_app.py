import streamlit as st
import pandas as pd
import math
from pathlib import Path
from string import ascii_letters, digits, punctuation
import random
st.title('Генератор паролей')
length = st.slider('Длина пароля', 8, 24, 16)
special = st.checkbox('Использовать спецсимволы')
if st.button('Создать'):
    char = ascii_letters + digits
    if special:
        char += punctuation
    password = "".join(random.choices(char, k = length))
    st.code(password, language = 'test')
