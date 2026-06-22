import os

# Налаштування
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-key-here")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TON_WALLET_ADDRESS = os.getenv("TON_WALLET_ADDRESS", "")

# Платформи для пошуку
PLATFORMS = ["upwork", "freelancer", "kwork", "telegram_channels"]

# Ваші навички
SKILLS = ["Python", "AI", "data analysis", "content writing", "українська мова"]

print("Config loaded")
