import os
import telebot
from dotenv import load_dotenv

load_dotenv()

class TelegramNotifier:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if self.token and self.chat_id:
            self.bot = telebot.TeleBot(self.token)
        else:
            self.bot = None
            print("⚠️ TelegramNotifier: Токен або Chat ID не налаштовані")

    def send_message(self, message: str):
        """Надсилає повідомлення в Telegram"""
        if not self.bot:
            print(f"📨 [Telegram] {message}")
            return False
        
        try:
            self.bot.send_message(self.chat_id, message, parse_mode="HTML")
            return True
        except Exception as e:
            print(f"❌ Помилка надсилання в Telegram: {e}")
            return False

    def send_error(self, error_message: str, context: str = ""):
        """Спеціальне сповіщення про помилку"""
        msg = f"🚨 <b>ПОМИЛКА в Job Agent Team</b>\n\n"
        if context:
            msg += f"<b>Контекст:</b> {context}\n\n"
        msg += f"<b>Деталі:</b> {error_message}\n\n"
        msg += f"🕒 Час: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        return self.send_message(msg)

    def send_success(self, message: str, details: dict = None):
        """Сповіщення про успішне завершення циклу"""
        msg = f"✅ <b>УСПІХ: Цикл Job Agent завершено</b>\n\n"
        msg += f"{message}\n\n"
        
        if details:
            for key, value in details.items():
                msg += f"<b>{key}:</b> {value}\n"
        
        msg += f"\n🕒 Час: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        return self.send_message(msg)
