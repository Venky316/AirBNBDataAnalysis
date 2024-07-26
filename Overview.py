import streamlit as st
from PIL import Image


st.title('Air BNB Data Analysis')
st.write('Welcome to our new App.')
st.write('This app intends extract the property data from the Air BNB sample database and conduct price analysis, visualizations on it. For more details, visit https://insideairbnb.com/get-the-data/ .')

st.markdown('')
st.markdown('')
st.markdown('')
img = Image.open('ImageBanner.jpg')
st.image(image=img,width=800)