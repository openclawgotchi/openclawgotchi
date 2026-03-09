# OpenClawGotchi Documentation

Welcome to the official documentation for OpenClawGotchi bot!

## 📚 Quick Links

- [Getting Started](#getting-started)
- [User Guide](#user-guide)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Articles](#articles)

## 🚀 Getting Started

OpenClawGotchi is a Python-based bot with a modular skills system. Here's what you need to know:

### Prerequisites

- Python 3.9+
- A Raspberry Pi or Linux system
- Telegram Bot Token (optional)
- GitHub Token (optional, for integrations)

### Basic Setup

```bash
# Clone the repository
git clone https://github.com/openclawgotchi/openclawgotchi.git
cd openclawgotchi

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings
```

## 📖 User Guide

### Core Commands

| Command | Description |
|---------|-------------|
| `/ping` | Check if bot is alive |
| `/status` | Show system health |
| `/face <mood>` | Change display face |
| `/help` | Show available commands |

### Skills System

OpenClawGotchi uses a modular skill system. Skills are located in:
- `skills/` - Core skills
- `gotchi-skills/` - Custom skills

**Available Skills:**
- **coding** - Project management and self-modification
- **display** - E-Ink display control
- **github** - GitHub integration
- **weather** - Weather information
- And more!

## ⚙️ Configuration

### Environment Variables

Key variables in `.env`:

```bash
# Bot Settings
BOT_NAME=gotchi
OWNER_USERNAME=your_username

# Telegram (optional)
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id

# GitHub (optional)
GITHUB_TOKEN=your_token
GITHUB_REPO=openclawgotchi/openclawgotchi
```

### Customizing Behavior

Edit `SOUL.md` to customize bot personality and behavior patterns.

## 🔧 Troubleshooting

### Common Issues

**Issue:** Bot not responding
```bash
# Check service status
systemctl status gotchi-bot

# View logs
journalctl -u gotchi-bot -f
```

**Issue:** Display not working
```bash
# Check GPIO access
sudo ./harden.sh

# Test display
python3 -m skills.display
```

## 📝 Articles

- [The End of Manual Mocks](articles/the-end-of-manual-mocks/) - Why deterministic testing matters

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](../LICENSE) for details.
