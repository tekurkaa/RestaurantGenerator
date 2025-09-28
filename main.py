import streamlit as st
import langchain_helper as lch
import re

# Page title
st.title("🍽️ Restaurant Generator")
st.markdown("---") # divider

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "American", "Mexican", "Chinese", "Japanese"))

if cuisine:
    # Generate response
    response = lch.generate_restaurant_name_and_items(cuisine)
    restaurant_name = response['restaurant_name']
    menu_items_raw = response['menu_items']
    if isinstance(menu_items_raw, list):
        menu_items_raw = menu_items_raw[0]  
    menu_items = [re.sub(r'^\d+\.\s*', '', item).strip() for item in menu_items_raw.split("\n") if item.strip()]

    # Restaurant name
    st.header(restaurant_name)
    
    # Menu section
    st.subheader("📜 Menu")

    # Display menu items
    for idx, item in enumerate(menu_items, start=1):
        st.write(f"{idx}. {item}")

    st.markdown("---")
    st.caption("✨ Generated with AI")