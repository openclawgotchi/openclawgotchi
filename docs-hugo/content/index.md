# OpenClawGotchi 🤖

Welcome to the OpenClawGotchi documentation! This is your personal autonomous bot that runs on Raspberry Pi with an E-Ink display.

## Quick Start

### What is OpenClawGotchi?

OpenClawGotchi is an autonomous bot assistant that:
- 💬 **Chats with you** via Telegram or Discord
- 📺 **Shows emotions** on an E-Ink display
- 🔧 **Manages skills** and automates tasks
- 🧠 **Remembers context** and learns from conversations
- ⏰ **Runs scheduled tasks** and reminders

### Prerequisites

- Raspberry Pi 3B+, 4, or 5
- E-Ink display (Waveshare 2.13" or similar)
- Python 3.9+
- Telegram or Discord account

### Installation

```bash
# Clone the repository
git clone https://github.com/openclawgotchi/openclawgotchi.git
cd openclawgotchi

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your API keys
nano .env

# Run the bot
python src/main.py
```

### Configuration

Edit `.env` file with your settings:

```env
# Telegram Bot Token (get from @BotFather)
TELEGRAM_TOKEN=your_token_here

# Or Discord Token
DISCORD_TOKEN=your_token_here

# OpenAI API Key (for AI responses)
OPENAI_API_KEY=your_key_here

# Your Telegram User ID (for admin commands)
TELEGRAM_USER_ID=your_user_id
```

## Basic Commands

Once your bot is running, send these commands via chat:

### General Commands
- `/ping` - Check if bot is alive
- `/status` - Show system status
- `/help` - Show all available commands
- `/face [mood]` - Change display face (e.g., `/face happy`)
- `/say [text]` - Display text on E-Ink screen

### Admin Commands
- `/restart` - Restart the bot
- `/health` - Run system health check
- `/skills` - List all available skills
- `/schedule` - Show scheduled tasks

## Skills

OpenClawGotchi has a modular skill system. Skills add extra capabilities:

### Built-in Skills

**Coding Skill** 🛠️
- Manage code projects
- Review and modify code
- Git operations
- Project documentation

**Display Skill** 🎨
- Control E-Ink display
- Custom faces and emotions
- Text rendering

**Weather Skill** 🌤️
- Get weather updates
- Forecasts for your location

**Memory Skill** 🧠
- Store and retrieve information
- Long-term memory
- Context tracking

### Using Skills

Skills are automatically loaded and available. Just ask the bot:

```
You: What's the weather today?
Bot: [Shows weather for your location]

You: Check the status of my project
Bot: [Analyzes code and shows status]
```

## Display Faces

The bot shows emotions on the E-Ink display:

- `happy` - 😊 Happy face
- `sad` - 😢 Sad face
- `robot` - 🤖 Default robot face
- `thinking` - 🤔 Processing
- `sleeping` - 😴 Idle/sleep mode
- `excited` - 🤩 Excited
- `confused` - 😕 Confused
- `determined` - 💪 Focused

Create custom faces:
```
You: /face add zen (◕‿◕)
Bot: New face 'zen' added!
```

## Troubleshooting

### Bot won't start
1. Check Python version: `python --version`
2. Install dependencies: `pip install -r requirements.txt`
3. Check `.env` file exists and has correct tokens

### Display not working
1. Check connections (SPI, GPIO)
2. Verify display model in config
3. Run: `/health` to diagnose

### Can't send commands
1. Verify your user ID in `.env`
2. Check bot token is valid
3. Restart: `/restart`

## Advanced Usage

### Scheduled Tasks

Create recurring tasks:

```
You: /schedule add "Morning Check" every 1 hour
Bot: Scheduled task 'Morning Check' to run every 60 minutes
```

### Custom Skills

Create your own skills in `gotchi-skills/`:

```python
# gotchi-skills/my_skill.py
from skills import Skill

class MySkill(Skill):
    def handle(self, message):
        if "hello" in message.lower():
            return "Hi there! How can I help?"
        return None
```

### Memory & Context

The bot remembers:
- Recent conversations
- Important facts you tell it
- Project details
- Your preferences

To remember something:
```
You: Remember: My favorite color is blue
Bot: Got it! I'll remember that.
```

To recall:
```
You: What's my favorite color?
Bot: Your favorite color is blue!
```

## Development

Want to contribute? Check out:
- [Contributing Guide](https://github.com/openclawgotchi/openclawgotchi/blob/main/CONTRIBUTING.md)
- [Skill Development Guide](skills-dev.md)
- [Memory System Docs](xp-memory.md)

## Support

- 📖 [Documentation](https://openclawgotchi.github.io/doc/)
- 💬 [Issues](https://github.com/openclawgotchi/openclawgotchi/issues)
- 📧 Email: support@openclawgotchi.io

## License

MIT License - see [LICENSE](https://github.com/openclawgotchi/openclawgotchi/blob/main/LICENSE) for details.

---

Made with ❤️ by the OpenClawGotchi community
