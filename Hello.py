import streamlit as st

TITLE = "Hello, Everyone!"
st.set_page_config(page_title=TITLE, page_icon=':smiley:')

st.title(TITLE)

st.write('This is a simple Streamlit app.')

st.sidebar.title("Select a page")