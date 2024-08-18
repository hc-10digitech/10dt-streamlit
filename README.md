# Streamlit Development
Streamlit is a rapid application development environment: which means it is good at quickly developing applications. Streamlit mostly focuses on creating data analysis and data visualisation
applications. 

## What is this project?
This project is a multi-page streamlit web application. Each page has some base code (some more than others), that you will add to so that you can create a working page. 

## The pages
* **Hello.py** - This is the landing or home page of the application. It is a good place for you to check out how to put things like images, text, headings etc. onto a page. All the other pages are stored inside the pages folder
* **1_🔢_Processing_Input.py** - This page gives you the chance to use your skills from the Introduction to Python excercises to accept numerical input and perform calculations. The template includes two input boxes, but you might choose to solve a problem that incorporates more.
* **2_📊_Graph.py** - This page is to demonstrate creating a graph. The sample code loads data from a CSV spreadsheet file for you, which you will use to create one (or more) graphs.
* **3_📈_Interactive_Graph.py** - This page is for you to create an interactive graph. You might use code from the previous page to load a spreadsheet, or find one of your own with interesting data.
* **4_🛜_Using_Live_Data.py** - This page demonstrates how to gather data from a public API. APIs allow you to get easily processed data from live data sources.

As part of the project, you will also add at least one additional page. This is your opportunity to experiment further: either by combining some of the skills you have learned, or by trying something new.

# Streamlit Basics
## How do I run this project?
You can run this project using GitHub Codespaces. This will allow you to run the project in the cloud, without needing to install anything on your computer. The project already has the settings for your environment set up, so you can just click the green "Code" button and select "Open with Codespaces".

## How do I run this project locally?
To run this project locally, other than having Python installed, you need to install the streamlit package. This will take some time to process - as it has a number of dependant packages. Once you have installed streamlit, you can run the project by typing `streamlit run Hello.py` in the terminal.

## Streamlit Components
Streamlit has a number of components that you can use to create your applications. Some of the most common components are:
* st.title() - This is used to create a title for your page
* st.header() - This is used to create a header for your page
* st.subheader() - This is used to create a subheader for your page
* st.image() - This is used to display an image on your page
* st.write() - This is used to write text to your page
* st.text_input() - This is used to create a text input box
* st.number_input() - This is used to create a number input box
* st.button() - This is used to create a button
* st.columns() - This is used to create columns on your page

## Where do I get help?
We will go through each of the different tools in class, but anytime you are looking to add additional functionality to your applications, the best place to go is the [Streamlit Documentation at https://docs.streamlit.io/](https://docs.streamlit.io/)
