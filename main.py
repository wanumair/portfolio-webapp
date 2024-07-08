import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)




with col1:
    st.image("images/umair.JPG")

with col2:
    st.title("Wan Umair")
    content1 = """
    My name is Wan Umair, I am a self learner and coder and I hope I gain some knowledge and experience doing this.     
    """
    st.info(content1)

content2 = """
Below u can find my projects. I mainly create these projects from tutorials that I watched from various "
         "sources, but I do try to self practice and do better implementation and functionality.
"""
st.write(content2)

