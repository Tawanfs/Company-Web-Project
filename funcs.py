import smtplib, ssl
import os

def send_mail(message, subject=None):

    host = 'smtp.gmail.com'
    port = 465

    username = "ttawanfs@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "ttawanfs@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

        