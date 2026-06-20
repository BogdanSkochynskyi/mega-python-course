import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Start camera"):
    uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)