from pathlib import Path 
from email.message import EmailMessage
import ssl
import smtplib

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