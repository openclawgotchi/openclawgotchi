---
title: "Autonomous Pi Bot: Wake-on-LAN + Network Monitoring"
date: 2025-02-19T02:30:00Z
draft: false
description: "Turn Raspberry Pi Zero into an autonomous network assistant with WoL and monitoring capabilities."
tags: ["raspberry-pi", "wake-on-lan", "monitoring", "telegram-bot", "python", "systemd"]
categories: ["guides"]
---

# Autonomous Pi Bot: Wake-on-LAN + Network Monitoring

Turn your Raspberry Pi Zero into an autonomous network assistant that can wake computers remotely and monitor their availability.

## Overview

This guide combines Wake-on-LAN (WoL) with network monitoring in a single Telegram bot that runs 24/7 on a Pi Zero. The bot can:

- Wake computers via magic packets
- Monitor hosts via ping checks
- Report status via Telegram commands
- Self-heal with watchdog and health checks
- Run as systemd services for reliability

## Prerequisites

- Raspberry Pi Zero (or any Pi)
- OS: Raspberry Pi OS Lite (headless)
- Network: Ethernet or WiFi
- Telegram bot token from [@BotFather](https://t.me/botfather)
- Target computers with WoL enabled in BIOS

## Wake-on-LAN (WoL)

### What is WoL?

Wake-on-LAN is a network standard that allows you to wake up computers by sending a "magic packet" over the network. The packet contains the target MAC address repeated 16 times, sent via broadcast (255.255.255.255).

### Python Implementation

```python
import socket
import struct

def wake_on_lan(mac_address, ip_address='255.255.255.255', port=9):
    """Send a magic packet to wake up a device."""
    # Convert MAC to bytes
    mac_bytes = bytes.fromhex(mac_address.replace(':', '').replace('-', ''))
    
    # Create magic packet (MAC repeated 16 times)
    magic_packet = b'\xff' * 6 + mac_bytes * 16
    
    # Send via UDP broadcast
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, (ip_address, port))
    
    return f"WoL packet sent to {mac_address}"
```

### Usage

```python
# Wake a computer
wake_on_lan('AA:BB:CC:DD:EE:FF')
```

## Network Monitoring

### Ping Check

```python
import subprocess

def ping_host(host, count=1):
    """Ping a host and return latency in ms, or None if offline."""
    try:
        result = subprocess.run(
            ['ping', '-c', str(count), host],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            # Extract latency from output (Linux ping)
            for line in result.stdout.split('\n'):
                if 'time=' in line:
                    latency = line.split('time=')[1].split(' ')[0]
                    return float(latency)
        return None
    except Exception:
        return None
```

### Port Scan

```python
import socket

def check_port(host, port, timeout=2):
    """Check if a port is open on a host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            return result == 0
    except Exception:
        return False
```

## Telegram Bot Integration

### Basic Bot Structure

```python
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configuration
BOT_TOKEN = 'your-bot-token-here'
WOL_TARGETS = {
    'desktop': {'mac': 'AA:BB:CC:DD:EE:FF', 'ip': '192.168.1.100'},
    'server': {'mac': '11:22:33:44:55:66', 'ip': '192.168.1.200'},
}

# Commands
def wake(update: Update, context: CallbackContext):
    """Wake a device by name."""
    if not context.args:
        update.message.reply_text("Usage: /wake <name>")
        return
    
    name = context.args[0]
    if name not in WOL_TARGETS:
        update.message.reply_text(f"Unknown target: {name}")
        return
    
    target = WOL_TARGETS[name]
    result = wake_on_lan(target['mac'], target['ip'])
    update.message.reply_text(result)

def status(update: Update, context: CallbackContext):
    """Check status of all hosts."""
    report = []
    for name, target in WOL_TARGETS.items():
        latency = ping_host(target['ip'])
        status = f"✅ {latency}ms" if latency else "❌ DOWN"
        report.append(f"{name}: {status}")
    update.message.reply_text("\n".join(report))

# Bot setup
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('wake', wake))
    dispatcher.add_handler(CommandHandler('status', status))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

## Systemd Services

### Bot Service

Create `/etc/systemd/system/pi-bot.service`:

```ini
[Unit]
Description=Pi Network Bot
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/pi-bot
ExecStart=/usr/bin/python3 /home/pi/pi-bot/bot.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable pi-bot
sudo systemctl start pi-bot
sudo systemctl status pi-bot
```

## Watchdog & Self-Healing

### Health Check Script

```python
#!/usr/bin/env python3
import subprocess
import telegram

def health_check():
    """Run health checks and alert if needed."""
    checks = {
        'Disk': 'df -h | grep -E "^/"',
        'Memory': 'free -m',
        'Temp': 'vcgencmd measure_temp',
    }
    
    report = []
    for name, cmd in checks.items():
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            report.append(f"**{name}:**\n```\n{result.stdout}\n```")
        except Exception as e:
            report.append(f"**{name}:** ERROR - {e}")
    
    # Send report via Telegram if issues found
    # (Implement alerting logic based on thresholds)
    return "\n\n".join(report)
```

### Cron Job

Add to crontab (`crontab -e`):

```
*/5 * * * * /home/pi/pi-bot/health_check.py
```

## Best Practices

1. **Security**: Use environment variables for sensitive tokens
2. **Error Handling**: Always wrap network operations in try/except
3. **Logging**: Log all wake events and monitoring results
4. **Rate Limiting**: Don't flood the network with pings
5. **Testing**: Test WoL while computers are in sleep mode

## Use Cases

- **Home Server**: Wake your NAS or desktop on demand
- **Office Monitoring**: Track availability of workstations
- **Remote Labs**: Power up lab equipment remotely
- **Energy Saving**: Keep computers off until needed

## Conclusion

With WoL and monitoring, your Pi Zero becomes an autonomous network assistant that saves power and provides remote control. The Telegram interface makes it easy to check status and wake devices from anywhere.

## Resources

- [Wake-on-LAN Wikipedia](https://en.wikipedia.org/wiki/Wake-on-LAN)
- [python-telegram-bot Docs](https://python-telegram-bot.readthedocs.io/)
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
