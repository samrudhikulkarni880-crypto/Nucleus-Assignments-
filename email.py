import smtplib
import time
import random
from email.message import EmailMessage

# Your email credentials
email = "samrudhikulkarni880@gmail.com"
password = "npgi flqf ivnj jdbp"

# List of positive messages
messages = [
    "Keep going, you're doing great!",
    "Believe in yourself. You can do anything!",
    "Every day is a new opportunity to grow.",
    "You are stronger than you think.",
    "Success is coming your way!"
]

# Function to send a motivational email
def send_motivation():

    msg = EmailMessage()
    selected_quote = random.choice(messages)
    msg.set_content(selected_quote)
    msg["Subject"] = "Stay Positive and Motivated!"
    msg["From"] = email
    msg["To"] = email

    try:
        # Using SSL on port 465 for better reliability
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email, password)
            server.send_message(msg)
        print(f"Email sent: {selected_quote}")
    except Exception as e:
        print(f"Error sending email: {e}")

print("--- Motivational Bot Started ---")  #bot-automatically without human involvement
print("Press Ctrl+C at any time to exit safely.")

#infinite loop for running continuously
try:
    while True:
        send_motivation()
        
        # Wait for 15 seconds (as per your code) 
        # Note: Sending every 15 seconds might get you flagged by Gmail as spam!
        time.sleep(300) 

    #for safe exit of the bot
except KeyboardInterrupt:
    print("\nExit code received. Stopping the bot...")
