from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.delete_state(message.from_user.id)
    bot.reply_to(message, f"Привет, {message.from_user.username}! Введи /help чтобы получить справку.")
