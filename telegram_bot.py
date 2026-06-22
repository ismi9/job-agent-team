import telebot

class TelegramNotifier:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token) if token else None
    
    def send_notification(self, message):
        if self.bot:
            # self.bot.send_message(CHAT_ID, message)
            print("📨 Сповіщення в Telegram:", message)
        else:
            print("Telegram bot не налаштовано.")
