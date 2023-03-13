import streamlit as st
import pandas as pd
import datetime
from pathlib import Path 
from email.message import EmailMessage
import ssl
import smtplib
from streamlit_extras.stateful_button import button

# Findmore emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# -------- HEADER SECTION ---------


st.image("https://www.tinsa.es/wp-content/uploads/2016/03/logo-tinsa-facebook.jpg")
st.title("TINSA TELEWORK WEBSITE")



if button("Button 1", key="button1"):
    if button("Button 2", key="button2"):
        if button("Button 3", key="button3"):
            st.write("All 3 buttons are pressed")


col1, col2, col3 = st.columns(3)

with col1:
    #st.image("https://ncrefuge.org/wp-content/uploads/2019/11/new-icon.png")
    button('Nueva Petición', key = "button1")
    

with col2:
    #st.image("https://static9.depositphotos.com/1003938/1123/v/950/depositphotos_11233144-stock-illustration-funny-cartoon-manager.jpg")
    button('Managers', key = "button2")

with col3:
    #st.image("https://play-lh.googleusercontent.com/WL9oSrJxfO6XDrSnuERVcjFXN--XztDibPGtAxIJsJBfm2ZAv4WvkR5yFuOcFKKR0_A=w240-h480-rw")
    button('Estado Petición', key = "button3")




if button('Nueva Petición', key = "button1"):
        employee_code = st.text_input("Código empleado:")
        percent = st.slider('Porcentaje:', 0, 100, 5)
        format_telework = reg_can = st.radio('Type of change?',
                                            ('Semanas enteras', 'Por días'))      