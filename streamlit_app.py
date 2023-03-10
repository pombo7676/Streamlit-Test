import streamlit as st
import pandas as pd
import datetime
from pathlib import Path 

# Findmore emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# -------- HEADER SECTION ---------


st.image("https://www.tinsa.es/wp-content/uploads/2016/03/logo-tinsa-facebook.jpg")
st.title("TINSA HR HEADCOUNT")
st.subheader("App to update registrations and cancellations")

st.write("[Official Website](https://www.tinsa.es/)")

reg_can = st.radio(
    'Type of change?',
    ('Registration', 'Voluntary Resignation', 'Dismisall'))


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    

if reg_can == "Registration":


    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Personal info:")
        first_name = st.text_input('First Name:')
        last_name = st.text_input('Last Name:')
        sex = st.radio(
            'Sex',
            ('Female', 'Male'))
        nation = st.text_input('Nationality:')
        date_birth = st.date_input("Birth Date:", min_value = datetime.date(1950, 1, 1))
        email = st.text_input('Email:')
        telephone = st.text_input('Telephone:')

    with col2:
        st.header("Registration:")
        employee_code = st.text_input("Employee Code:")
        reg_date = st.date_input("Registration Date:")
        type_contract = st.radio('Full/Part Time?',
    ('Full Time', 'Part Time'))
    

    with col3:
        st.header("Contract")

else:
    st.header("Personal info:")
    employee_code = st.text_input("Employee Code:")
    
   
agree = st.checkbox('Everything complete')
if agree == 1:
    if st.button('Apply'):
        new_row = [employee_code,
                   last_name,
                   first_name,
                   sex,
                   nation,
                   date_birth,
                   email,
                   telephone,
                   reg_date,
                   type_contract]

        
        
        dataframe.loc[len(dataframe.index)] = new_row

        st.write(dataframe)
                
        csv = dataframe.to_csv(index = False).encode('utf-8')


        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Test.csv',
            mime='text/csv')
