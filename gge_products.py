import streamlit as st
import json
from utils import apply_custom_theme

apply_custom_theme()

def display_products(product_list):    
    for product in product_list:
        url = product["affiliate_key"]
        image_url = product["image_url"]

        # Fetch affiliate URL securely
        url = st.secrets.get("affiliate_links", {}).get(affiliate_key)

        # Skip product if secret is missing
        if not url:
            st.warning(f"Affiliate link missing for {product.get('name')}")
            continue

        with st.expander(product["name"], expanded=True):
            col_img, col_btn = st.columns([1, 4])  # Adjust ratio as needed
            
            with col_img:
                st.image(image_url, width=180)
            
            with col_btn: 
                st.markdown(" ")  # small spacing
                 
                button_html = f"""  
                    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                        <a href="{url}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
                            <button style="
                                background-color: #FF9900;
                                color: white;
                                padding: 10px 20px;
                                border: none;
                                border-radius: 5px;
                                font-size: 16px;
                                cursor: pointer;
                            ">
                                CLICK HERE FOR DETAILS & BUYING THE PRODUCT
                            </button>
                        </a>    
                    </div>
                """
                st.markdown(button_html, unsafe_allow_html=True)

# Main Streamlit function
def products_navigation():
    def load_products():
        with open("gge_affiliate_products", "r") as f:
            return json.load(f)

    products = load_products()
    st.markdown("")
    st.write("Discover curated products that empower your journey — proudly promoted by GrindGlowElite (GGE).")

    st.markdown("""
    <style>
    /* Fix background and padding for tab headers */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #f0f2f6;
        border-radius: 8px;
        padding: 0.5rem;
    }

    /* Fix selected tab background */
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        border-radius: 8px;
        padding: 10px;
        margin-right: 5px;
        font-weight: bold;
        color: #000;
    }

    /* Highlight selected tab */
    .stTabs [aria-selected="true"] {
        background-color: #d6e4ff !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

    tab_names = [
        "All", "Professional Services", "Digital Products", "Digital Marketing", "Digital Strategy",
        "Retail Products - Niche"
    ]

    tabs = st.tabs(tab_names)

    for i, category in enumerate(tab_names):
        with tabs[i]:
            if category == "Retail Products - Niche":
                st.subheader("Explore Niche Retail Products")
                sub_tab_names = [
                    "All", "Health & Wellness",
                    "Beauty", "Books", "Tools", "Technology"
                ]
                sub_tabs = st.tabs(sub_tab_names)
                for j, sub_cat in enumerate(sub_tab_names):
                    with sub_tabs[j]:
                        if sub_cat == "All":
                            combined = (
                                products.get("Health & Wellness", []) +
                                products.get("Beauty", []) +
                                products.get("Books", []) +
                                products.get("Tools", []) +
                                products.get("Technology", [])
                            )
                            display_products(combined)
                        else:
                            display_products(products.get(sub_cat, []))
            elif category == "All":
                all_products = sum(products.values(), [])
                display_products(all_products)
            else:
                display_products(products.get(category, []))