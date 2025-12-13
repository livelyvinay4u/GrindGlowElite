import streamlit as st # type: ignore
from utils import apply_custom_theme

apply_custom_theme()

def home_navigation():
    #st.markdown("<h1 style='text-align: center;'>🌟 Welcome to <span style='color:#FF6F61;'>GrindGlowElite</span> 🌟</h1>", unsafe_allow_html=True)
    #st.markdown("<h2 style='text-align: center;'>🌟 Welcome to GrindGlowElite</span> 🌟</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; font-style: italic;'>Grind smart. Glow bold. Thrive with the best picks and insights.</h5>", unsafe_allow_html=True)

    st.write("""
    **"Welcome to GrindGlowElite (GGE), your gateway to excellence"**. At GGE, we turn ambition into action. Whether you're building your side hustle, scaling your business, or just looking for smart finds to fuel your goals — you're in the right place.

    Explore handpicked products, exclusive deals, practical insights, and actionable blogs — all designed to help you grow, glow, and thrive.
    """)

    st.markdown("""
    - 💼 **Curated Products, Powered by Affiliates**  
    - 🔥 **Insider Deals & Actionable Insights**  
    - 💬 **Real-Time Support, Always On**  
    - 📲 **Built for Hustlers, Optimized for Growth**
    """)

    st.markdown("<h4 style='margin-top: 30px; text-align: center;'>Grind with purpose. Glow with pride. Succeed with the best.</h4>", unsafe_allow_html=True)
    #st.markdown("<h4 style='text-align: center; font-style: italic;'>Grind with purpose. Glow with pride. Succeed with the best.</h4>", unsafe_allow_html=True)