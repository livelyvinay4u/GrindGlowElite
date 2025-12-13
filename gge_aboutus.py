import streamlit as st
from utils import apply_custom_theme

apply_custom_theme()

def aboutus_navigation():
    #st.header("About Us")
    #st.write("Welcome to GrindGlowElite — where hustle meets harmony.")

    st.markdown("### 🧠 Who We Are")
    st.write("""
    **GGE** is more than just a brand—it's a mindset. Built for people who are creators, hustlers, dreamers and online shoppers, we’re here to spotlight the best products that align with your lifestyle and ambitions.
    """)

    st.markdown("### 🚀 Our Mission")
    st.write("""
    To empower everyday shoppers by curating high-quality, value-driven products that inspire confidence, creativity, and success.
    """)

    st.markdown("### 💡 What We Do")
    st.write("""
    We research and promote products that:
    - ✅ Solve real problems  
    - ✅ Enhance productivity or lifestyle  
    - ✅ Offer great value for money  
    - ✅ Are perfect for sharing on social media  

    Whether you're into tech, wellness, fashion, or digital tools—we’ve got something that fits your niche.
    """)

    st.markdown("### 📲 Why Instagram & Social Media?")
    st.write("""
    Because that’s where the hustle lives. We use platforms like Instagram to:
    - 📸 Share product reviews and demos (where available)  
    - 🤝 Connect with our audience  
    - 🔗 Drive affiliate engagement through authentic storytelling
    """)

    st.markdown("### 🤝 Affiliate Transparency")
    st.write("""
    We may earn commissions when you purchase through our links—but we only promote what we truly believe in. Your trust is our top priority.
    """)