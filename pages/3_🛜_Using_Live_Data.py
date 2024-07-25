import streamlit as st
import requests
import streamlit as st
import requests

# Define a function to load data from a given URL
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

# Allow the user to select a data source from a dropdown menu
selected_source = st.selectbox("Select a data source", ["AFL Ladder", "Fortnite News"])

# Load data based on the selected data source
if selected_source == "AFL Ladder":
    # Set a custom header for the AFL Ladder API request
    header = {'User-Agent': "Mr Matheson's streamlit app for Yr 10 Digitech - geoff.matheson@education.vic.gov.au"}
    # Load data from the AFL Ladder API
    data = load_data('https://api.squiggle.com.au/?q=standings', header=header)
elif selected_source == "Fortnite News":
    # Load data from the Fortnite News API
    data = load_data('https://fortnite-api.com/v2/news')

# Display the loaded data on the app
st.write(data)

# Display a success message in the sidebar
st.sidebar.success("Select a page from the list above")

