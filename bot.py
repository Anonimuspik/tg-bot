import telebot
import os

TOKEN = os.getenv("8767700934:AAEszzWFEbCfsNehEd2Ewv6GxKzmDqB8FwY")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def handle(message):
    if "!ресты" in message.text.lower():
        bot.reply_to(message, "Рест 1\nРест 2\nРест 3")

bot.polling()
