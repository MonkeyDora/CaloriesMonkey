import streamlit as st
from utils import configuration_page

st.set_page_config(
    page_title="Main",
    page_icon="🏠"
)

configuration_page()

st.title("🚀SnapMetrix")
st.image("home.jpg", use_container_width=True)
st.write("""
    Have you ever thought that the food we consume greatly affects our survival? Have you ever imagined that our favorite foods will be the foods we avoid the most in the future? 

Currently, many people lack knowledge about the importance of nutrition for their bodies. We realize that many people always want to try to live a healthy life, but do not have enough access to know about it.

Our vision and mission is to help people achieve a healthy lifestyle. We realize that many people have difficulty finding foods that are nutritionally appropriate so we are here to help you manage the nutrition your body needs.

We are here to help the community in providing information about food nutrition.
""")



