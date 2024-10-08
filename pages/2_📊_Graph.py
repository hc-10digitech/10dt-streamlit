import streamlit as st
import pandas as pd
TITLE = "Graphing from a Spreadsheet"
@st.cache_data
def load_data():
    return pd.read_csv('gameconsoles.csv')

st.set_page_config(page_title=TITLE, page_icon=':bar_chart:', layout="wide")

st.title(TITLE)

st.write('This is a simple Streamlit app that reads a spreadsheet and graphs the data. (or at least it will be)')
st.write("At the moment all it does is show the data from the spreadsheet")
df = load_data()
st.dataframe(df)

st.sidebar.success("Select a page from the list above")