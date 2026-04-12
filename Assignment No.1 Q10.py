import smtplib
from datetime import datetime

def send_email(word):
    sender = "faizanshakh3241@gmail.com"
    password = "vnos nhzs oyud pene"
    receiver = "gawaishreyash027@gmail.com"
    message = f"Subject: ALERT!\n\nWord: {word}\nTime: {datetime.now()}"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
        print("Email Sent Successfully!")
    except Exception as e:
        print("Error:", e)

send_email("Python")