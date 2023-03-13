import streamlit as st
import pandas as pd
import datetime
from pathlib import Path 
from email.message import EmailMessage
import ssl
import smtplib

# Findmore emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# -------- HEADER SECTION ---------


st.image("https://www.tinsa.es/wp-content/uploads/2016/03/logo-tinsa-facebook.jpg")
st.title("TINSA TELEWORK WEBSITE")
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fehorus.com%2Fteleworking%2F&psig=AOvVaw1tg1FkUKbGsJxlCDCq80bH&ust=1678792645336000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCODi747k2P0CFQAAAAAdAAAAABAD")


col1, col2, col3 = st.columns(3)

with col1:
    st.button('Nueva Petición')  

with col2:
    st.button('Managers')

with col3:
    st.button('Estado Petición')
    
    
if st.button('Nueva Petición'):
    employee_code = st.text_input("Código empleado:")
    percent = st.slider('Porcentaje:', 0, 100, 5)
    format_telework = reg_can = st.radio('Type of change?',
                                         ('Semanas enteras', 'Por días'))



    email_emisor = 'inigo.larrea@tinsa.com'
    email_contrasena = 'ndlcrxjymcgfiojr'

    email_receptor = 'inigo.larrea@tinsa.com'

    asunto = 'TELEWORK PETITION FROM ' + employee_code
    cuerpo = 'El empleado ' + employee_code + ' ha pedido teletrabajo con un porcetaje del ' + percent + '. Y con formato de ' + format_telework + '.'


    em = EmailMessage()

    em['From'] = email_emisor
    em['To'] = email_receptor
    em['Subject'] = asunto
    em.set_content(cuerpo)

    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
        smtp.login(email_emisor, email_contrasena)
        smtp.sendmail(email_emisor, email_receptor, em.as_string())