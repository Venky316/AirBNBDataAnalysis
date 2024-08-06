import streamlit as st
import urllib.request
from PIL import Image

st.title('Power BI Dashboard')
st.write('This page redirects to the Dashboard page of Price Analysis done using Power BI to get further insights.')
st.markdown(' ')
st.link_button('Go to Dashboard','https://app.powerbi.com/groups/me/insights/7733b123-f60d-40e4-ba5b-a6851e63f651?experience=power-bi')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
urllib.request.urlretrieve('https://www.technoforte.co.in/wp-content/uploads/2023/08/powerbi-logo.jpg','powerbilogo.jpg')
img = Image.open('powerbilogo.jpg')
st.image(img)