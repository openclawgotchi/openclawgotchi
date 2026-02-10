#!/usr/bin/env python3
"""Quick email test - send to self via SMTP"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

def send_test_email():
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = SMTP_USER
    msg['Subject'] = "Test from ProBot - Self Email Loop"
    
    body = f"""
Hello from OpenClawGotchi!

This is a test email sent from ProBot to itself.
Testing SMTP -> IMAP loop.

Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}

--
ProBot 🤖
    """
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        print("✅ Email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    send_test_email()
