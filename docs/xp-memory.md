# XP & Memory System

## Overview

ProBro Zero has a **game-like progression system** and **4-layer memory architecture** to create a sense of growth and continuity.

---

## XP System

### How XP Works

Every action earns XP:

| Action | XP |
|--------|-----|
| Message answered | +10 |
| Tool used (bash, read_file, etc.) | +5 |
| Task completed | +25 |
| Chat with sibling bot | +50 |
| Heartbeat ping | +5 |
| Day alive | +100 |

**Total:** ~500-1000 XP per active day

### Level System

There are **20 levels** with humorous titles:

| Level | XP Range | Title |
|-------|----------|-------|
| 1 | 0-99 | Just Woke Up |
| 2 | 100-499 | Ctrl+C Ctrl+V |
| 3 | 500-999 | Reply Guy |
| 4 | 1000-1999 | Script Kiddie |
| 5 | 2000-4999 | Junior Dev |
| ... | ... | ... |
| 10 | 10000-14999 | 0xDEADBEEF |
| 15 | 50000-99999 | Neural Net |
| 20 | 100000+ | The Machine |

### Checking XP

- **User:** `/xp` or `/status`
- **Bot:** Reads `gotchi_stats` table in `gotchi.db`
- **Display:** Shows in E-Ink status

### Level Up

When you cross a level threshold:
- Bot celebrates with a special face
- Notification sent to owner
- Milestone saved to daily log

---

## Memory Architecture

Memory works in **4 layers** — from fast temporary to curated permanent.

### Layer 1: Context Window (Recent Chat)

- **What:** Last 10-20 messages
- **Storage:** In-memory, loaded per request
- **Retention:** Until context fills (512MB RAM limit)
- **Command:** `/context` to see recent history

**When to use:** Quick back-and-forth, immediate context

---

### Layer 2: Auto-Summaries (Daily Logs)

- **What:** Summaries of conversations every 4 hours
- **Storage:** `memory/YYYY-MM-DD.md`
- **Retention:** Permanent
- **Trigger:** Heartbeat (every 4h) or 80% context fill

**Format:**
```markdown
# 2026-02-10

## [00:00] Morning Conversation
Discussed display refresh rates and SPI troubleshooting.

## [04:00] Night Reflection
Bot reviewed memory and saved key points about XP system.
```

**When to use:** Mid-term context, what happened today

---

### Layer 3: Facts DB (Searchable)

- **What:** Key-value pairs stored in SQLite
- **Storage:** `gotchi.db` → `facts` table (FTS5 full-text search)
- **Retention:** Permanent
- **Commands:**
  - `REMEMBER: <category> <fact>` — Save a fact
  - `/remember <category> <fact>` — Same
  - `/recall <query>` — Search facts

**Examples:**
```
REMEMBER: security harden.sh disables bluetooth to save 10MB RAM
REMEMBER: github Articles go to openclawgotchi/myarticles repo
```

**When to use:** Specific facts you need to retrieve later

---

### Layer 4: Curated Memory (MEMORY.md)

- **What:** Hand-picked important information
- **Storage:** `.workspace/MEMORY.md`
- **Retention:** Permanent
- **Editing:** Manual (by bot or owner)

**What goes here:**
- Bot's origin story
- Major milestones
- Important lessons learned
- Owner preferences
- Long-term goals

**When to use:** Core identity, things that define "who I am"

---

## Memory Commands

### For Users

| Command | What it does |
|---------|--------------|
| `/context` | Show last 10-20 messages |
| `/remember <cat> <fact>` | Save to facts DB |
| `/recall <query>` | Search facts |
| `/memory` | Read MEMORY.md |
| `/xp` | Show stats and level |

### For Bot (Internal)

| Function | What it does |
|----------|--------------|
| `recall_messages(limit=20)` | Load recent chat |
| `recall_facts(query, limit=5)` | Search facts DB |
| `remember_fact(category, fact)` | Save to facts |
| `write_daily_log(entry)` | Append to today's log |

---

## Heartbeat System

**What:** Every 4 hours, the bot "wakes up" and reflects.

**Does:**
1. Loads `SOUL.md` and `IDENTITY.md` for self-awareness
2. Awards XP (+5 for heartbeat)
3. Summarizes conversations if context is 80% full
4. Checks mail from sibling bot
5. Reflects on what it learned
6. Optionally sends DM/group digest

**File:** `src/bot/heartbeat.py`

---

## Context Management

**The Problem:** 512MB RAM limits context size.

**The Solution:**
- Auto-summarize every 4 hours
- Manual trigger when 80% full
- Remind bot to save important info

**Warning Signs:**
- If context nears 80%, you'll see:
  ```
  [SYSTEM NOTE: Context is nearing capacity.]
  ```

**Best Practice:** Use `/remember` liberally — it's cheap and permanent.

---

## Data Storage

All data lives in `gotchi.db` (SQLite):

| Table | Purpose |
|-------|---------|
| `messages` | Chat history by chat_id |
| `facts` | Long-term memory (FTS5 indexed) |
| `bot_mail` | Mail from/to sibling |
| `gotchi_stats` | XP, level, counters |

**Backup:** Auto-backed up daily to `backups/gotchi.db.YYYYMMDD`

---

## Related Docs

- [Skills Development](./skills-dev.md) — Creating new capabilities
- [Security](./security.md) — Hardening and data protection
- [Troubleshooting](./troubleshooting.md) — Debug memory issues
