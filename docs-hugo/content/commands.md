# Bot Commands Reference 📋

Complete list of all available commands in OpenClawGotchi.

## Table of Contents

- [Basic Commands](#basic-commands)
- [Display Commands](#display-commands)
- [System Commands](#system-commands)
- [Admin Commands](#admin-commands)
- [Memory Commands](#memory-commands)
- [Skill Commands](#skill-commands)
- [Schedule Commands](#schedule-commands)

---

## Basic Commands

### `/ping`
Check if the bot is online and responding.

**Usage:**
```
/ping
```

**Response:**
```
pong! 🏓
```

### `/help`
Show help message with all available commands.

**Usage:**
```
/help
```

---

## Display Commands

### `/face [mood]`
Change the E-Ink display to show a specific emotion/mood.

**Available Moods:**
- `happy` - 😊 Happy face
- `sad` - 😢 Sad face
- `robot` - 🤖 Default robot face
- `thinking` - 🤔 Processing/Thinking
- `sleeping` - 😴 Sleep mode
- `excited` - 🤩 Excited
- `confused` - 😕 Confused
- `determined` - 💪 Focused
- `zen` - (◕‿◕) Zen mode
- `apologetic` - 😿 Sorry face

**Usage:**
```
/face happy
/face robot
```

### `/say [text]`
Display custom text on the E-Ink screen.

**Usage:**
```
/say Hello World!
/say Temperature: 22°C
```

**Note:** Text is limited to ~20 characters depending on display size.

---

## System Commands

### `/status`
Show current system status including CPU, memory, disk, and temperature.

**Usage:**
```
/status
```

**Response:**
```
📊 System Status:
CPU: 15%
Memory: 45%
Disk: 62%
Temperature: 42°C
Uptime: 2 days, 4 hours
```

### `/health`
Run comprehensive health check on the bot system.

**Usage:**
```
/health
```

**Checks:**
- Internet connectivity
- Disk space
- CPU temperature
- Service status
- Recent errors

### `/restart`
Restart the bot service (admin only).

**Usage:**
```
/restart
```

---

## Admin Commands

### `/skills`
List all available skills and their status.

**Usage:**
```
/skills
```

**Response:**
```
Available Skills:
✅ coding - Code management
✅ display - E-Ink control
✅ weather - Weather updates
✅ memory - Long-term memory
```

### `/logs`
Show recent bot logs.

**Usage:**
```
/logs
```

**Optional:** Specify number of lines:
```
/logs 50
```

### `/git [command]`
Run git commands in the project repo.

**Usage:**
```
/git status
/git log --oneline -5
```

---

## Memory Commands

### `/remember [fact]`
Store important information in long-term memory.

**Usage:**
```
/remember My favorite color is blue
/remember Server IP: SERVER_IP
```

### `/recall [query]`
Retrieve information from memory.

**Usage:**
```
/recall favorite color
/recall server IP
```

### `/forget [fact]`
Remove specific fact from memory.

**Usage:**
```
/forget old password
```

---

## Skill Commands

### `/skill enable [name]`
Enable a specific skill.

**Usage:**
```
/skill enable weather
```

### `/skill disable [name]`
Disable a specific skill.

**Usage:**
```
/skill disable github
```

---

## Schedule Commands

### `/schedule list`
Show all scheduled tasks.

**Usage:**
```
/schedule list
```

**Response:**
```
Scheduled Tasks:
1. Daily Backup - every 24 hours
2. Health Check - every 1 hour
```

### `/schedule add [name] [interval]`
Add a new scheduled task.

**Intervals:**
- `every X minutes`
- `every X hours`
- `in X minutes` (one-time)
- `in X seconds` (one-time)

**Usage:**
```
/schedule add "Morning Check" every 1 hour
/schedule add "Restart" in 30 minutes
```

### `/schedule remove [task_id]`
Remove a scheduled task.

**Usage:**
```
/schedule remove 1
```

---

## Chat Commands

These work without the `/` prefix - just chat naturally!

### Questions
```
What's the weather?
Check my email
What's on my calendar?
Tell me a joke
```

### Tasks
```
Remind me to call Mom at 5pm
Check the server status
Update my project
```

### Information
```
What can you do?
How long have you been running?
What skills do you have?
```

---

## Tips & Tricks

1. **Quick Status Check**: Just say "status" without the `/` prefix
2. **Natural Conversation**: Most commands work in natural language
3. **Custom Faces**: Create your own with `/face add [name] [kaomoji]`
4. **Bulk Commands**: Separate multiple commands with `&&`
   ```
   /face robot && /say System online
   ```

---

## Keyboard Shortcuts (Telegram)

- `/` - Show command menu
- Tab - Auto-complete command (in supported clients)

---

Need more help? Check the [main documentation](index.md) or [open an issue](https://github.com/openclawgotchi/openclawgotchi/issues).
