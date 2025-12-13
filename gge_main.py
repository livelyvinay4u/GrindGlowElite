import streamlit as st  # type: ignore
from PIL import Image # type: ignore
from io import BytesIO
from pathlib import Path

# Set page config

st.set_page_config(
    page_title="Grind Glow Elite",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

import base64
import smtplib
from gge_home import home_navigation
from gge_aboutus import aboutus_navigation
from gge_products import products_navigation
from gge_contactus import contactus_navigation
from gge_blogs import blogs_navigation
from email.message import EmailMessage
from utils import apply_custom_font

apply_custom_font()

# Custom background and styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #f3e7ff, #d0f0ff, #e0ffe9);
            background-attachment: fixed;
        }
            
        section[data-testid="stSidebar"] {
            background: linear-gradient(135deg, #f3e7ff, #d0f0ff, #e0ffe9);
        }
            
        .app-header {
            display: flex;
            align-items: center;
            gap: 20px;
            padding: 10px 0;
        }

        .app-title h1 {
            margin: 0;
            font-size: 2em;
        }

        .app-title p {
            margin: 5px 0 0 0;
            font-size: 1.1em;
            color: gray;
        }

        @media (max-width: 768px) {
            .app-header {
                flex-direction: column;
                text-align: center;
            }
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Products", "Blog", "Contact Us"])

# Load and convert image to base64
@st.cache_data
def get_image_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()
    return img_base64

# Get base64 string

img_path = Path("Photos") / "GGE_Logo.jpg"
img_base64 = get_image_base64(img_path)
#img_base64 = get_image_base64("Photos\GGE_Logo.jpg")

# Properly formatted HTML with f-string
html_content = f"""
<div style="display: flex; align-items: center;">
    <img src="data:image/jpeg;base64,{img_base64}" alt="Logo" style="height: 80px; margin-right: 15px;"/>
    <h1 style="margin: 0; font-size: 3em; font-weight: bold;">
        <span style="text-decoration: underline; color: black;">G</span><span style="color: #333333;">rind</span>
        <span style="text-decoration: underline; color: black;">G</span><span style="color: #FFA500;">low</span>
        <span style="text-decoration: underline; color: black;">E</span><span style="color: #4B0082;">lite</span>
    </h1>
</div>
"""
st.markdown(html_content, unsafe_allow_html=True)

# ───── Page Routing ─────
if page == "Home":
    home_navigation()

elif page == "About Us":
    aboutus_navigation()

elif page == "Products":
    products_navigation()

elif page == "Blog":
    #st.header("Under Development")
    blogs_navigation()

elif page == "Contact Us":
    contactus_navigation()

