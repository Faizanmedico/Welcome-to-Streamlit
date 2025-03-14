import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write('Hi!')

st.write('Hi!')


st.title("Sultan IT Web")
st.header("Sultan Ahmed")
with st.sidebar:
    st.radio("Select one:", [1, 2])

st.text("Fixed width text")
st.markdown("_Markdown_")
st.code("for i in range(8): foo()")
st.html("<p>Hi!</p>")
st.html("<h1>Hi! Sultan Ahmed</h1>")


col1, col2, col3 = st.columns([3, 1, 1])
# Two equal columns:
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# Three different columns:
col1, col2, col3 = st.columns([3, 1, 1])


tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")







st.button("Click me")
st.radio("Pick one", ["cats", "dogs"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.camera_input("Take a picture")
st.color_picker("Pick a color")



"""app.py"""
import streamlit as st

# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)

st.title("Bean counter :paw_prints:")

addend = st.number_input("Beans to add", 0, 10)
if st.button("Add"):
    st.session_state.beans += addend
st.markdown(f"Beans counted: {st.session_state.beans}")

