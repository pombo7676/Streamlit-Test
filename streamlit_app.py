import streamlit as st
import pandas as pd

# Findmore emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# -------- HEADER SECTION ---------


st.image("https://www.tinsa.es/wp-content/uploads/2016/03/logo-tinsa-facebook.jpg")
st.title("TINSA HR HEADCOUNT")
st.subheader("App to update registrations and cancellations")

st.write("[Official Website](https://www.tinsa.es/)")

reg_can = st.selectbox(
    'Type of change?',
    ('Registration', 'Voluntary Resignation', 'Dismisall'))


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Personal info:")
   name = st.text_input('Name:')
   last_name = st.text_input('Last Name:')
   sex = st.selectbox(
    'Sex',
    ('Female', 'Male'))
   nation = st.text_input('Nationality:')
   date_birth = st.date_input("Birth Date:")
   email = st.text_input('Email:')
   telephone = st.text_input('Telephone:')

with col2:
   st.header("Registration:")
   
   

with col3:
   st.header("Contract")
   
   