#!/usr/bin/env python3
"""
Read emails from IMAP server (Zoho)
Usage: python3 tools/read_email.py [--limit N] [--unread-only]
"""

import imaplib
import email
from email.header import decode_header
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# IMAP settings
IMAP_HOST = "imap.zoho.eu"
IMAP_PORT = 993
IMAP_USER = os.getenv("SMTP_USER", "openclawgotchi@zohomail.eu")
IMAP_PASS = os.getenv("SMTP_PASS")

def decode_header_value(header_value):
    """Decode email header value"""
    if not header_value:
        return ""
    
    decoded_parts = []
    for part, encoding in decode_header(header_value):
        if isinstance(part, bytes):
            decoded_parts.append(part.decode(encoding or 'utf-8', errors='replace'))
        else:
            decoded_parts.append(str(part))
    return ''.join(decoded_parts)

def read_emails(limit=5, unread_only=False):
    """Read emails from IMAP server"""
    
    if not IMAP_PASS:
        print("❌ SMTP_PASS not set in .env (needed for IMAP)")
        return False
    
    try:
        # Connect to IMAP server
        print(f"🔌 Connecting to {IMAP_HOST}:{IMAP_PORT}...")
        mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        mail.login(IMAP_USER, IMAP_PASS)
        mail.select("INBOX")
        
        # Build search criteria
        criteria = "UNSEEN" if unread_only else "ALL"
        print(f"🔍 Searching for: {criteria}")
        
        status, messages = mail.search(None, criteria)
        
        if status != "OK":
            print("❌ Search failed")
            return False
        
        # Get message IDs
        email_ids = messages[0].split()
        total = len(email_ids)
        
        if total == 0:
            print("📭 No messages found")
            return True
        
        # Limit results
        email_ids = email_ids[-limit:]  # Get most recent
        print(f"📬 Found {total} messages, showing last {len(email_ids)}:\n")
        
        # Fetch each email
        for msg_id in reversed(email_ids):  # Newest first
            status, msg_data = mail.fetch(msg_id, "(RFC822)")
            
            if status != "OK":
                continue
            
            # Parse email
            raw_email = msg_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            
            # Extract fields
            subject = decode_header_value(email_message.get("Subject", "(No subject)"))
            from_addr = decode_header_value(email_message.get("From", "(Unknown)"))
            date = email_message.get("Date", "(Unknown date)")
            
            print(f"📧 From: {from_addr}")
            print(f"   Subject: {subject}")
            print(f"   Date: {date}")
            
            # Get body
            body = ""
            if email_message.is_multipart():
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        try:
                            body = part.get_payload(decode=True).decode('utf-8', errors='replace')
                        except:
                            body = "(Failed to decode body)"
                        break
            else:
                try:
                    body = email_message.get_payload(decode=True).decode('utf-8', errors='replace')
                except:
                    body = "(Failed to decode body)"
            
            # Show preview (first 200 chars)
            if body:
                preview = body.strip().replace('\n', ' ')[:200]
                print(f"   Preview: {preview}...")
            
            print()
        
        # Close connection
        mail.close()
        mail.logout()
        return True
        
    except imaplib.IMAP4.error as e:
        print(f"❌ IMAP error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Read emails from Zoho IMAP")
    parser.add_argument("--limit", type=int, default=5, help="Max emails to show")
    parser.add_argument("--unread-only", action="store_true", help="Only unread emails")
    
    args = parser.parse_args()
    
    read_emails(limit=args.limit, unread_only=args.unread_only)
