import streamlit as st
import  pandas

st.set_page_config()

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

#to seperate the data in csv using semicolon
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")