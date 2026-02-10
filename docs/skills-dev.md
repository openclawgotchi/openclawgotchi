# Skills Development Guide

## Overview

ProBro Zero has a **two-tier skill system**:

1. **Active Skills** — Loaded and ready to use (in `src/skills/`)
2. **Reference Skills** — Passive knowledge base (in `openclaw-skills/`)

---

## Active Skills

Active skills are Python modules in `src/skills/` that can be executed.

### Current Active Skills

| Skill | Description | Commands |
|-------|-------------|----------|
| `coding` | Modify bot's own code, understand project structure | `/code`, `/refactor` |
| `display` | Control E-Ink display | `FACE:`, `SAY:`, `DISPLAY:` |
| `weather` | Get weather via wttr.in (no API key) | `/weather` |
| `system` | Pi administration: power, services, monitoring | `/system`, `/health` |
| `discord` | Send messages to Discord | `/discord` |

### Skill Structure

An active skill is a Python file with:

```python
# src/skills/your_skill.py

SKILL_INFO = {
    "name": "your_skill",
    "description": "What this skill does",
    "commands": ["command1", "command2"],
    "requires": []  # Dependencies: ["wifi", "api_key", etc.]
}

def main(action, *args):
    """
    Main entry point
    action: the command/verb to execute
    args: additional parameters
    """
    if action == "command1":
        return do_command1(args)
    # ...
```

### Registering a New Skill

1. **Create the file** in `src/skills/your_skill.py`
2. **Add to registry** in `src/skills/__init__.py`:

```python
from .your_skill import SKILL_INFO as YOUR_SKILL_INFO

ACTIVE_SKILLS = [
    # ... existing skills
    YOUR_SKILL_INFO,
]
```

3. **Restart the bot:** `/restart` or `safe_restart()`

---

## Reference Skills

Reference skills live in `openclaw-skills/` — they're documentation and examples from the OpenClaw ecosystem.

### Why Reference Skills?

- **50+ skills** available for reference
- Most require **macOS** or specific CLIs not available on Pi
- Use them as **learning material** or **adapt to Linux/Pi**

### Example Reference Skills

| Skill | Description | Platform |
|-------|-------------|----------|
| `alfred` | Alfred workflows | macOS |
| `keyboard` | Keyboard control | macOS |
| `notion` | Notion integration | Any (needs API) |
| `spotify` | Spotify control | macOS |

### Using Reference Skills

1. **Search:** `search_skills("query")` — find capabilities
2. **Read:** `read_skill("skill_name")` — get documentation
3. **Adapt:** If compatible, implement as active skill

---

## Skill Development Best Practices

### DO's

- Keep skills **modular** — one file per skill
- Return **structured responses** — dicts or formatted strings
- Handle **errors gracefully** — try/except with clear messages
- Document **requirements** in `SKILL_INFO`
- Use **built-in tools** first (see `TOOLS.md`)

### DON'Ts

- Don't hardcode secrets — use `.env`
- Don't block the event loop — use async or timeouts
- Don't duplicate existing tools — check `ARCHITECTURE.md` first
- Don't make heavy operations — Pi has limited RAM/CPU

---

## Examples

### Simple Skill: Timezones

```python
# src/skills/timezones.py

import zoneinfo
from datetime import datetime

SKILL_INFO = {
    "name": "timezones",
    "description": "Get time in different zones",
    "commands": ["time"],
    "requires": []
}

def main(action, *args):
    if action == "time":
        zone = args[0] if args else "UTC"
        try:
            tz = zoneinfo.ZoneInfo(zone)
            return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
        except:
            return f"Unknown timezone: {zone}"
    return "Usage: /time <timezone>"
```

### Discord Skill Integration

```python
# src/skills/discord.py

import os
import requests

SKILL_INFO = {
    "name": "discord",
    "description": "Send messages to Discord",
    "commands": ["discord"],
    "requires": ["DISCORD_WEBHOOK_URL"]
}

def main(action, *args):
    if action == "send":
        webhook = os.getenv("DISCORD_WEBHOOK_URL")
        if not webhook:
            return "Error: DISCORD_WEBHOOK_URL not set"
        
        message = " ".join(args)
        requests.post(webhook, json={"content": message})
        return f"Sent to Discord: {message}"
```

---

## Related Docs

- [XP & Memory System](./xp-memory.md) — How bot learns
- [E-Ink Display](./eink-display.md) — Face and display control
- [Security](./security.md) — Hardening and permissions
