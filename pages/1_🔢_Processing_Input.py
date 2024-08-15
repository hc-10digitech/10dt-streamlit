import streamlit as st

st.header("Using Inputs")

col1, col2 = st.columns(2)

with col1: 
    number_1 = st.number_input("Enter First Number", step=1)
    number_2 = st.number_input("Enter Second Number", step=1)
    
    
with col2:
    st.write("Output Information will go here")