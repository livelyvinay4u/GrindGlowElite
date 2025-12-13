import streamlit as st
from pathlib import Path
import re
from datetime import datetime
import os

from utils import apply_custom_font

apply_custom_font()

st.markdown("""
    <style>
        /* Stack columns on mobile by forcing them to full width */
        @media (max-width: 768px) {
            .element-container:nth-child(odd) > div {
                width: 100% !important;
            }
            .element-container:nth-child(even) > div {
                width: 100% !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Main function to be called from Main.py
def blogs_navigation():
    #st.set_page_config(page_title="Glow Blog", layout="wide")
    #st.title("📝 Glow Blog")
    st.markdown("""
    <style>
        .blog-header h1 {
            text-align: left;
            font-size: 2em;
            margin-bottom: 0.2em;
        }

        @media (max-width: 768px) {
            .blog-header h1 {
                font-size: 2em;
            }
        }
    </style>
    <div class='blog-header'>
        <h1>📝 Glow Blog</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("Welcome to the Grind Glow Elite blog — your source for insights, inspiration, and elite-level growth.")

    # Folder that holds blog Markdown files
    BLOG_FOLDER = Path(__file__).parent / "Blogs"

    if not BLOG_FOLDER.exists():
        st.warning("Blog folder not found.")
        return

    # Read and parse blog files
    blog_files = [f for f in BLOG_FOLDER.iterdir() if f.suffix == ".md"]

    blogs = [parse_blog(f) for f in blog_files]
    blogs.sort(key=lambda x: x["date"], reverse=True)

    # Display tiles (3 per row)
    cols = st.columns(3)

    for idx, blog in enumerate(blogs):
        col = cols[idx % 3]
        with col:
            st.markdown("------")
            st.markdown(f"<h3 style='margin-bottom: 0.2em;'>{blog['title']}</h3>", unsafe_allow_html=True)
            st.caption(blog["date"].strftime("%B %d, %Y"))
            st.write(blog["summary"])
            with st.expander("Read More"):
                st.markdown(blog["content"])
            st.markdown("------")

# Helper function to parse blog metadata
def parse_blog(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    title_match = re.search(r"^Title:\s*(.*)", content, re.MULTILINE)
    date_match = re.search(r"^Date:\s*(.*)", content, re.MULTILINE)
    summary_match = re.search(r"^Summary:\s*(.*)", content, re.MULTILINE)

    title = title_match.group(1).strip() if title_match else "Untitled"
    date_str = date_match.group(1).strip() if date_match else "2025-01-01"
    summary = summary_match.group(1).strip() if summary_match else ""

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        date = datetime(2025, 1, 1)

    split_content = content.split("---", 1)
    full_content = split_content[1].strip() if len(split_content) > 1 else ""

    return {
        "title": title,
        "date": date,
        "summary": summary,
        "file": file_path,
        "content": full_content
    }