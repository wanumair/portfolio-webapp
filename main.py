import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/umair.JPG")

with col2:
    st.title("Wan Umair")
    content = """
wan umair
    """
    st.info(content)

