# utils.py
import streamlit as st

def apply_custom_font():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif !important;
        }
        </style>
    """, unsafe_allow_html=True)