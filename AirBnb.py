import streamlit as st
from PIL import Image

overview_page = st.Page('Overview.py',title='Overview')
explore_page = st.Page('Explore Properties.py',title='Explore Properties')
analyse_page = st.Page('Price Analysis.py',title='Price Analysis')
dashboard_page = st.Page('Dashboard.py',title='Dashboard')

pg = st.navigation([overview_page,explore_page,analyse_page,dashboard_page])
st.set_page_config(page_title='Air BNB Data Analysis',layout='wide',initial_sidebar_state='auto')
pg.run()