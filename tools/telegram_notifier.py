import os
import time
from datetime import datetime

try:
    import telebot
except ImportError:
    telebot = None


class TelegramNotifier:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN", "")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
        self.bot = None
        if telebot and self.token:
            self.bot = telebot.TeleBot(self.token)

    def send_message(self, text: str, parse_mode: str = "HTML") -> bool:
        if not self.bot or not self.chat_id:
            print(f"[Notifier] {text}")
            return False
        try:
            self.bot.send_message(self.chat_id, text, parse_mode=parse_mode)
            return True
        except Exception as e:
            print(f"[Notifier] Send error: {e}")
            return False

    def send_success(self, title: str, details: dict = None) -> bool:
        msg = f"✅ <b>{title}</b>\n"
        msg += f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        if details:
            for k, v in details.items():
                msg += f"• {k}: {v}\n"
        return self.send_message(msg)

    def send_error(self, context: str, error: str = None) -> bool:
        msg = f"❌ <b>Помилка: {context}</b>\n"
        msg += f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        if error:
            msg += f"<code>{error}</code>\n"
        return self.send_message(msg)