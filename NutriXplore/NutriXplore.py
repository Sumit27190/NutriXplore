import streamlit as st

st.set_page_config(page_title="NutriXplore", page_icon="🍽️", layout="wide")

st.markdown("<h1 style='text-align: center; color: #D32F2F;'>🍽️ Welcome to NutriXplore</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>An AI-powered tool to analyze Indian food nutrition and health suitability.</p>", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1613145991416-5b45f8e0f9c6", use_container_width=True)


st.info("Navigate from the sidebar to explore!")
