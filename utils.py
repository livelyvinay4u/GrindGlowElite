import streamlit as st

def apply_custom_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [data-testid="stAppViewContainer"] {
            background-color: #FFFFFF;
            color: #000000;
            font-family: 'Poppins', sans-serif;
        }

        /* Text elements */
        p, span, label, div {
            color: #000000 !important;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #F5F5F5;
        }

        </style>
    """, unsafe_allow_html=True)
