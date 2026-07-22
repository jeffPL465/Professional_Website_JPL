import streamlit as st
from PIL import Image
import pathlib
import os

st.set_page_config(layout="wide")
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Jeffrey Ponce Lopes")
    st.title("Professional Portfolio")

with col2: 
    st.image('Pics_Vids/test_image1.png', width=500)


# Add sidebar with buttons for each area
with st.sidebar:
    st.title("Welcome Chuds")
    st.text("This shit is wild")

    st.button('touch me =)')
    

