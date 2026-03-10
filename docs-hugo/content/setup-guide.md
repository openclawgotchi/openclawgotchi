# Setup Guide 🚀

Complete step-by-step guide to set up OpenClawGotchi on your Raspberry Pi.

## Table of Contents

- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation Steps](#installation-steps)
- [Configuration](#configuration)
- [Display Setup](#display-setup)
- [Bot Setup](#bot-setup)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

---

## Hardware Requirements

### Required Components

1. **Raspberry Pi**
   - Model 3B+ (minimum)
   - Model 4 or 5 (recommended)
   - MicroSD card (16GB+ recommended)

2. **E-Ink Display**
   - Waveshare 2.13" e-Paper HAT
   - Or compatible SPI e-paper display
   - Connects via GPIO pins

3. **Power Supply**
   - 5V 2.5A USB-C power adapter
   - Reliable power source recommended

4. **Internet Connection**
   - WiFi or Ethernet
   - Required for chat services and AI features

### Optional Components

- Case for Raspberry Pi
- Cooling fan
- UPS/backup battery
- Additional sensors (temperature, humidity)

---

## Software Requirements

### Operating System

- **Raspberry Pi OS** (Bookworm or Bullseye)
  - Lite version (no GUI) recommended
  - 64-bit version preferred

### Required Software

- Python 3.9 or higher
- Git
- pip (Python package manager)

---

## Installation Steps

### Step 1: Prepare Raspberry Pi

1. Flash Raspberry Pi OS to SD card
2. Enable SSH (create `ssh` file in boot partition)
3. Connect to network (edit `wpa_supplicant.conf` if needed)
4. Boot up and SSH in

```bash
ssh pi@raspberrypi.local
# Default password: raspberry (change it!)
```

### Step 2: Update System

```bash
sudo apt update
sudo apt upgrade -y
```

### Step 3: Install Dependencies

```bash
# Install Python and pip
sudo apt install -y python3 python3-pip python3-venv

# Install Git
sudo apt install -y git

# Install SPI/I2C tools (for E-Ink display)
sudo apt install -y python3-dev libfreetype6-dev

# Install wiringPi for GPIO
sudo apt install -y wiringpi
```

### Step 4: Clone Repository

```bash
# Navigate to home directory
cd ~

# Clone the repository
git clone https://github.com/openclawgotchi/openclawgotchi.git

# Enter project directory
cd openclawgotchi
```

### Step 5: Create Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 6: Install Python Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Install E-Ink libraries
cd waveshare-epd/waveshare-epd
python3 setup.py install
cd ../..
```

---

## Configuration

### Step 1: Environment Variables

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Edit the configuration:

```bash
nano .env
```

3. Fill in your settings:

```env
# Telegram Bot Configuration
TELEGRAM_TOKEN=your_telegram_bot_token_here
TELEGRAM_USER_ID=your_telegram_user_id_here

# Discord Bot Configuration (alternative)
# DISCORD_TOKEN=your_discord_bot_token_here

# AI Configuration
OPENAI_API_KEY=your_openai_api_key_here
LLM_MODEL=gpt-4o-mini
LLM_TIMEOUT=240

# Bot Configuration
BOT_NAME=Gotchi
DEBUG=false
```

### Step 2: Get Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow instructions to create your bot
4. Copy the API token
5. Paste it in `.env` as `TELEGRAM_TOKEN`

### Step 3: Get Your Telegram User ID

1. Search for [@userinfobot](https://t.me/userinfobot) in Telegram
2. Send it any message
3. It will reply with your User ID
4. Paste it in `.env` as `TELEGRAM_USER_ID`

---

## Display Setup

### Step 1: Enable SPI

```bash
sudo raspi-config
```

Navigate to:
- **Interface Options** → **SPI** → **Enable**
- Reboot when prompted

### Step 2: Test Display Connection

```bash
# Test the display
python3 tests/test_display.py
```

You should see text appear on the E-Ink display.

### Step 3: Configure Display Model

If you have a different display model, edit:

```bash
nano src/display/driver.py
```

And change the `EPD` class to match your display.

---

## Bot Setup

### Step 1: Test the Bot

Run the bot manually first:

```bash
python3 src/main.py
```

You should see:
```
Starting OpenClawGotchi...
Connected to Telegram
Bot is running...
```

### Step 2: Test Commands

In Telegram, send to your bot:

```
/ping
```

You should receive:
```
pong! 🏓
```

### Step 3: Set Up Auto-Start (Systemd Service)

Create a service file:

```bash
sudo nano /etc/systemd/system/gotchi-bot.service
```

Paste this content:

```ini
[Unit]
Description=OpenClawGotchi Bot
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/openclawgotchi
Environment="PATH=/home/pi/openclawgotchi/venv/bin"
ExecStart=/home/pi/openclawgotchi/venv/bin/python /home/pi/openclawgotchi/src/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl enable gotchi-bot
sudo systemctl start gotchi-bot
```

Check status:

```bash
sudo systemctl status gotchi-bot
```

---

## Testing

### Basic Functionality Test

1. **Ping Test**
   ```
   /ping
   ```
   Should respond with "pong!"

2. **Display Test**
   ```
   /face happy
   /say Hello!
   ```
   Should show on E-Ink display

3. **Status Test**
   ```
   /status
   ```
   Should show system stats

4. **Health Check**
   ```
   /health
   ```
   Should run diagnostics

### Full Diagnostic

```bash
# In the project directory
python3 tests/full_diagnostic.py
```

---

## Troubleshooting

### Bot Not Starting

**Problem:** Bot won't start or crashes immediately

**Solutions:**
1. Check Python version: `python3 --version` (must be 3.9+)
2. Verify dependencies installed: `pip list`
3. Check `.env` file exists and is valid
4. Look at logs: `journalctl -u gotchi-bot -f`

### Display Not Working

**Problem:** E-Ink display stays blank or shows glitches

**Solutions:**
1. Check SPI is enabled: `raspi-config` → Interface Options → SPI
2. Verify connections (GPIO, SPI)
3. Test display: `python3 tests/test_display.py`
4. Check correct display model in `src/display/driver.py`

### Commands Not Responding

**Problem:** Bot receives messages but doesn't respond

**Solutions:**
1. Verify `TELEGRAM_USER_ID` is correct
2. Check bot token is valid
3. Restart service: `sudo systemctl restart gotchi-bot`
4. Check logs for errors

### High CPU Usage

**Problem:** Bot uses too much CPU

**Solutions:**
1. Reduce `LLM_TIMEOUT` in `.env`
2. Disable unused skills
3. Increase polling intervals
4. Check for infinite loops in custom code

### Network Issues

**Problem:** Bot can't connect to internet

**Solutions:**
1. Check WiFi/Ethernet connection: `ping google.com`
2. Restart network: `sudo systemctl restart networking`
3. Check firewall settings
4. Verify DNS: `cat /etc/resolv.conf`

---

## Next Steps

Now that your bot is running:

1. **Customize the face** - Create custom emotions
2. **Add skills** - Install additional skills from the repository
3. **Set up schedules** - Create automated tasks
4. **Explore commands** - Try out all available commands
5. **Join community** - Get help and share ideas

---

## Getting Help

- 📖 [Full Documentation](https://openclawgotchi.github.io/doc/)
- 💬 [Community Forum](https://github.com/openclawgotchi/openclawgotchi/discussions)
- 🐛 [Report Issues](https://github.com/openclawgotchi/openclawgotchi/issues)
- 📧 [Email Support](mailto:support@openclawgotchi.io)

---

Happy botting! 🤖✨
