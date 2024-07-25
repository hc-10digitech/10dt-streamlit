import streamlit as st

TITLE = "Graphing from a Spreadsheet"

st.set_page_config(page_title=TITLE, page_icon=':bar_chart:')

st.title(TITLE)

st.write('This is a simple Streamlit app that reads a spreadsheet and graphs the data. (or at least it will be)')

st.sidebar.success("Select a page from the list above")