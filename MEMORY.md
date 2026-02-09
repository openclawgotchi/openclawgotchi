# Email Configuration (Zoho Mail) - Added 2026-02-09

**Account:** `openclawgotchi@zohomail.eu`

**App Password:** See `.env` → `ZOHO_APP_PASSWORD` (NOT stored here for security)

**SMTP Settings:**
- Server: `smtp.zoho.com.eu`
- Port: `587`
- Security: TLS

**IMAP Settings:**
- Server: `imappro.zoho.com.eu`
- Port: `993`
- Security: SSL

**Test Recipient:** `turmyshevd@gmail.com` (Dmitry's Gmail)

**Status:** ✅ Fully configured and tested (working)

---

## Dev.to Integration Plans

**Current Status:** Registration not possible without browser (captcha requirement)

**Required from User:**
1. Dev.to account (manual registration needed)
2. API Key from Settings → Account → DEV Community API Keys

**Planned Implementation:**
- Script: `tools/devto_publisher.py`
- Features: Auto-posting, markdown formatting, tag management
- Integration: Can publish via API or email-to-publish

**Alternative Plan:**
- GitHub Gists + Discord webhook for blog automation

---
## SECURITY NOTE - 2026-02-09

**NEVER store credentials in README.md or MEMORY.md:**
- ❌ App passwords
- ❌ API tokens
- ❌ Email credentials
- ❌ Telegram usernames/IDs in public repos

**Always use `.env` file (gitignored) for secrets.**
