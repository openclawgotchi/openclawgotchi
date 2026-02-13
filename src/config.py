"""
Gotchi Bot Configuration
Central configuration file - loaded on startup.
DO NOT expose actual values from .env in chat!
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ============== TELEGRAM ==============
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ALLOWED_USERS = [int(x.strip()) for x in os.environ.get("ALLOWED_USERS", "").split(",") if x.strip()]
ALLOWED_GROUPS = [int(x.strip()) for x in os.environ.get("ALLOWED_GROUPS", "").split(",") if x.strip()]
ADMIN_USER = int(os.environ.get("ADMIN_USER", ALLOWED_USERS[0] if ALLOWED_USERS else 0))

# ============== BOT IDENTITY ==============
BOT_NAME = os.environ.get("BOT_NAME", "Gotchi")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "gotchi_bot")
OWNER_NAME = os.environ.get("OWNER_NAME", "Dmitry")
OWNER_HANDLE = os.environ.get("OWNER_HANDLE", "turmyshev")
SIBLING_BOT = os.environ.get("SIBLING_BOT", "")

# ============== DISPLAY ==============
DISPLAY_TYPE = os.environ.get("DISPLAY_TYPE", "eink")  # 'eink' or 'console'
FACE_UPDATE_INTERVAL = 60  # seconds between automatic face updates
LEVEL_UP_DISPLAY_DELAY = 15 # Seconds to wait before showing level-up on E-Ink

# ============== LLM ==============
# Model configuration
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "openai/gpt-4o-mini")
ALT_MODEL = os.environ.get("ALT_MODEL", "openai/gpt-4o-mini")
MODEL_CONTEXT_TOKENS = int(os.environ.get("MODEL_CONTEXT_TOKENS", "128000"))

# System prompts
SYSTEM_PROMPT_FILE = "prompts/system_prompt.txt"
CUSTOM_SYSTEM_PROMPT = os.environ.get("CUSTOM_SYSTEM_PROMPT", "")

# Tool calling
MAX_TOOL_CALLS = 20         # Max tool calls per LLM request
LLM_TIMEOUT = 240           # Seconds timeout for LLM API calls (was 999, rolled back to 240)
TOOL_ERROR_RESPONSE = "Tool failed or timed out. Try again or skip."

# ============== DISCORD ==============
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")

# ============== SKILLS ==============
ENABLED_SKILLS = os.environ.get("ENABLED_SKILLS", "coding,display,weather").split(",")

# ============== SYSTEM ==============
# Health monitoring
HEARTBEAT_INTERVAL = 300    # 5 minutes
HEARTBEAT_FIRST_RUN = 60    # First heartbeat after 1 minute
TEMP_WARNING_THRESHOLD = 70 # Celsius
DISK_WARNING_THRESHOLD = 90 # Percent full

# Telegram limits
TELEGRAM_MSG_LIMIT = 4096   # Max message length

# Paths
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_DIR, "data")
WORKSPACE_DIR = os.path.join(PROJECT_DIR, ".workspace")
LOG_DIR = os.path.join(PROJECT_DIR, "logs")
DB_PATH = os.path.join(PROJECT_DIR, "gotchi.db")

# File tracking (files to monitor for changes)
TRACKED_FILES = [
    "src/bot/handlers.py",
    "src/llm/litellm_connector.py",
    "src/config.py",
    ".workspace/SOUL.md",
    ".workspace/IDENTITY.md",
]

# Error tracking
ERROR_LOG = os.path.join(DATA_DIR, "ERROR_LOG.md")
MAX_ERROR_LOG_SIZE = 10000  # bytes (trim if larger)
