import streamlit as st
import requests

# Define a function to load data from a given URL. We are caching the 
# data to avoid making multiple requests to the server
@st.cache_data()
def load_data(url, header = None):
    if header:
        response = requests.get(url, headers = header)
    else:
        response = requests.get(url)
    data = response.json()
    return data

# Set the title and page icon for the Streamlit app
TITLE = "Using Live Data"
st.set_page_config(page_title=TITLE, page_icon=':line_chart:')

# Display the title on the app
st.title(TITLE)

# Display an introductory message
st.write('''This is a Streamlit app that reads data from the internet, and uses interactive elements to present it
          (or at least it will be)''')

API_DICT = {
    "AFL Ladder": "https://api.squiggle.com.au/?q=standings",
    "Fortnite News": 'https://fortnite-api.com/v2/news',
    "Dog Pic of the Day": "https://dog.ceo/api/breeds/image/random",
    "Jelly Belly Flavours": "https://jellybellywikiapi.onrender.com/api/Beans/",
    "Deck of Cards": "https://deckofcardsapi.com/api/deck/new/draw/?count=5",
}


# Allow the user to select a data source from a dropdown menu
selected_source = st.selectbox("**Select a data source**", API_DICT.keys())

# Load data based on the selected data source
header = {'User-Agent': "Mr Matheson's streamlit app for Yr 10 Digitech - geoff.matheson@education.vic.gov.au"}
# Load data from the Selected API
data = load_data(API_DICT[selected_source], header=header)


# Display the loaded data on the app
st.write(data)

# Display a success message in the sidebar
st.sidebar.success("Select a page from the list above")

