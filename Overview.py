import streamlit as st
from PIL import Image

st.header('Air BNB Data Analysis')
st.markdown(' ')
st.write('Welcome to our new App.')
st.markdown(' ')
st.write('This app intends to extract the property data from the Air BNB sample database and conduct price analysis, visualizations on it. For more details, visit https://insideairbnb.com/get-the-data/ .')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
img = Image.open('ImageBanner.jpg')
st.image(img)
