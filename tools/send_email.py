#!/usr/bin/env python3
"""Send email via SMTP (Zoho)"""
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_address, subject, body):
    """Send email using SMTP"""
    msg = EmailMessage()
    msg['From'] = os.getenv('SMTP_USER')
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL(os.getenv('SMTP_HOST'), int(os.getenv('SMTP_PORT'))) as smtp:
            smtp.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASS'))
            smtp.send_message(msg)
        return True, "Email sent successfully!"
    except Exception as e:
        return False, str(e)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print("Usage: send_email.py <to> <subject> <body>")
        sys.exit(1)
    
    success, result = send_email(sys.argv[1], sys.argv[2], sys.argv[3])
    if success:
        print(f"✅ {result}")
    else:
        print(f"❌ {result}")
