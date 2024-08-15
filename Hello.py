import streamlit as st
# Setting TITLE as a constant that I use in multiple places
TITLE = "Hello, Everyone!"

# This line sets the title and icon of the page. 
st.set_page_config(page_title=TITLE, page_icon=':smiley',  layout="wide")

# This writes a title and normal text message
st.title(TITLE)
st.write('This is a simple Streamlit app.')

st.header("This is a header. It's smaller than the other one")
st.subheader("This is a subheader. It is even smaller.")

column1, column2 = st.columns(2)

with column1:
    st.write("This information is going on the left")
    if st.button("Press Me"):
        st.balloons()
    
with column2:
    st.write("This information is going on the right")
    st.image(image="./images/monster.png", caption="My Cute Monster")
    


# This adds the nice message below the sidebar navigation
st.sidebar.success("Select a page from the list above")