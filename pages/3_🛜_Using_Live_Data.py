import streamlit as st
import requests

@st.cache_data()
def load_data(url):
    header = {'User-Agent': "Mr Matheson's streamlit app for Yr 10 Digitech - geoff.matheson@education.vic.gov.au"}
    response = requests.get(url, headers = header)
    data = response.json()
    return data

TITLE = "Using Live Data"

st.set_page_config(page_title=TITLE, page_icon=':line_chart:')

st.title(TITLE)

st.write('''This is a Streamlit app that reads data from the internet, and uses interactive elements to present it
          (or at least it will be)''')

data = load_data('https://api.squiggle.com.au/?q=standings')

st.write(data)

st.sidebar.success("Select a page from the list above")

