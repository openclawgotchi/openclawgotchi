# Changelog

All notable changes to the OpenClawGotchi project will be documented in this file.

## [Unreleased] - 2026-02-09

### Added
- **`github_helper.py`**: GitHub API integration tool for creating repositories and checking repo existence via GitHub tokens
- **`tools/send_email.py`**: Email sending capability via SMTP using credentials from `.env`
- **Comprehensive workspace documentation**: 
  - `SOUL.md` — personality, vibe, values
  - `IDENTITY.md` — name, hardware, family, mission
  - `MEMORY.md` — curated long-term memories
  - `AGENTS.md` — agent roles and responsibilities
  - `ARCHITECTURE.md` — system architecture overview
  - `SAFETY.md` — safety rules and guidelines (132 lines)
  - `TOOLS.md` — available tools documentation
  - `BOT_INSTRUCTIONS.md` — bot operation instructions
  - `GUIDE-public-repos.md` — public repositories guide
  - `CHANGELOG.md` — change history
- **Heartbeat reflection system**:
  - `HEARTBEAT.md` — heartbeat logs
  - `HEARTBEAT_THOUGHTS.md` — thoughts during heartbeat checks
  - `BOOT.md` — system boot documentation
- **Daily memory logs**: Auto-saved conversation summaries in `memory/YYYY-MM-DD.md` format
  - 2025-01-14: Initial heartbeat (26 lines)
  - 2026-02-04 through 2026-02-09: Daily activity logs (500+ lines total)

### Changed
- **Root `MEMORY.md`**: Expanded with +40 lines of important project information
- **Self-documentation**: Bot now maintains comprehensive documentation of its own architecture, personality, and operation

## [Unreleased] - 2026-02-06

### Added
- **Soul & Identity in context**: `SOUL.md` and `IDENTITY.md` are now loaded during heartbeat for self-reflection, and lazily on identity-related questions. Bot can update them via `write_file()`.
- **`log_change` tool**: Bot maintains its own `.workspace/CHANGELOG.md` automatically after self-modifications.
- **`manage_service` tool**: Safe systemd wrapper with whitelist (gotchi-bot, ssh, networking, cron). Actions: status, restart, stop, start, logs.
- **`show_face` tool**: Wired into TOOL_MAP and TOOLS — was defined but never callable by the bot.
- **Self-Maintenance section** in BOT_INSTRUCTIONS.md: check_syntax → safe_restart flow, log_change after changes, health_check for diagnostics.
- **Heartbeat reflection logging**: Reflection text now saved to `memory/YYYY-MM-DD.md` daily logs.
- **Custom faces in display skill**: `add_custom_face()` documented, `data/custom_faces.json` mentioned.

### Added
- **Function Calling**: Enabled by default (`ENABLE_LITELLM_TOOLS=True`). The bot will now append tool usage (e.g., `remember_fact`, `check_mail`) to its replies.

### Changed
- **BOT_INSTRUCTIONS.md**: Slimmed from 86 to 58 lines — removed duplicate formatting examples, added Self-Knowledge Files and Self-Maintenance sections.
- **ARCHITECTURE.md**: Rewritten — correct 20 levels, 4h heartbeat interval, all current tools listed, context loading explained.
- **AGENTS.md**: Fixed `claude_bot.db` → `gotchi.db`, removed table formatting references.
- **IDENTITY.md**: Removed table mention from personality traits.
- **Telegram formatting**: NO markdown tables — use emoji + key:value in code blocks instead.
- **coding/SKILL.md**: Added all missing tools (log_change, manage_service, check_mail, etc.), updated self-modification flow with changelog step.
- **display/SKILL.md**: Added `add_custom_face` tool and custom faces info.
- **All `claude-bot` references → `gotchi-bot`** in gotchi-skills.
- **All `claude_bot.db` references → `gotchi.db`** across workspace, gitignore, skills.

### Removed
- `.workspace/hooks/bot_mail.py` — duplicated heartbeat.py mail logic, referenced wrong DB.
- `.workspace/.claude/commands/bot.md` — completely outdated (referenced old project structure).

## [Unreleased] - 2026-02-05

### Added
- **Passive Skill Knowledge**: `openclaw-skills/` directory is now treated as a searchable catalog rather than loading all skills into context. Bot can search for capabilities without RAM overhead.
- **New Active Skills**: 
  - `weather` — Get weather via wttr.in (no API key needed)
  - `system` — Pi administration: power, services, monitoring, backups
  - `discord` — Send messages to Discord via webhook or bot
- **Hardware Watchdog**: `harden.sh` now enables BCM2835 hardware watchdog (auto-reboot on system freeze after 15s).
- **3-Layer Protection**: Hardware watchdog + systemd restart + cron watchdog for maximum reliability.
- **Skill Discovery Tools**: `search_skills("query")` and `list_skills()` tools for finding capabilities in the skill catalog.
- **LLM Summarization**: Conversations are now automatically summarized by Gemini Flash during heartbeat and saved to daily logs.
- **Context Management**: New `/context` command shows context window usage with visual progress bar. Subcommands: `/context trim` (keep last 3 messages), `/context sum` (manual LLM summary).
- **Memory Auto-cleanup**: Database automatically prunes old messages to prevent infinite growth (keeps last 50 per chat).
- **Smarter History Summarization**: `extract_key_info()` now analyzes message content (questions, commands, actions) instead of simple truncation.
- **Functional Cron Jobs**: Scheduled tasks now trigger actual LLM reasoning. When a job fires, the bot can process the message and even trigger hardware commands (FACE, SAY) autonomously.
- **Onboarding System**: New `onboarding.py` logic and upgraded `BOOTS/README.md` with step-by-step first-run setup.
