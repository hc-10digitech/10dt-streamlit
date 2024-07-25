import streamlit as st

TITLE = "Creating an Interactive Graph"

st.set_page_config(page_title=TITLE, page_icon=':line_chart:')

st.title(TITLE)

st.write('''This is a Streamlit app that reads a spreadsheet and graphs the data, using interactive elements
          (or at least it will be)''')

st.sidebar.success("Select a page from the list above")