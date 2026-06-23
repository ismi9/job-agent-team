import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GROK_API_KEY = os.getenv("GROK_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
TON_WALLET_ADDRESS = os.getenv("TON_WALLET_ADDRESS", "")

# Agent settings
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock")  # mock | openai | grok
USE_MOCK_SCOUT = os.getenv("USE_MOCK_SCOUT", "true").lower() == "true"
USE_MOCK_EXECUTOR = os.getenv("USE_MOCK_EXECUTOR", "true").lower() == "true"

# Platforms
PLATFORMS = [
    "upwork",
    "freelancer",
    "kwork",
    "freelancehunt",
]

SKILLS = [
    "Python", "AI", "ML", "Data Science",
    "Telegram Bot", "Web Development",
    "DevOps", "Scraping", "Automation",
]