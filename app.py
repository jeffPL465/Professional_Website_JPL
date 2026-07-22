import streamlit as st
from PIL import Image
import pathlib
import os

st.set_page_config(layout="wide")
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Jeffrey Ponce Lopes")
    st.header("2026 Bachelors of Science | Electrical and Computer Engineering")
    st.text("Worcester Polytechnic Institute")

with col2: 
    st.image('Pics_Vids/test_image1.png', width=800)


# # Add sidebar with buttons for each area
# with st.sidebar:
#     st.title("Professional Portfolio")
#     st.text("Please click below to navigate each section")

#     st.button('touch me =)')
    
tab1, tab2, tab3 = st.tabs(["Work History", "Skills", "Past Projects"])

with tab1:
    st.header("Work History")

with tab2:
    st.header("Skills")

with tab3:
    st.header("Past Projects")
