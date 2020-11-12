import smtplib
from email.mime.text import MIMEText

def email(msg):
    senders = "xxxxxxxxxxx"
    receiver = "xxxxxxxx"
    msg = MIMEText(msg)
    if msg == "":
        msg = MImeText("No New upadate on the site.")
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.ehlo
    server.login("xxxxxxx","xxxxxxxx")
    server.sendmail(senders,receiver,msg.as_string())
    print("Message sent successfully.")