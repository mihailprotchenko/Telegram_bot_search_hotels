from telebot.types import Message
from loader import bot
from config_data.config import DEFAULT_COMMANDS
# Эхо хендлер, куда летят текстовые сообщения без указанного состояния


@bot.message_handler(func=lambda message: all(message.text[1:] not in el[0] for el in DEFAULT_COMMANDS))
def bot_echo(message: Message):
    bot.delete_state(message.from_user.id)
    bot.reply_to(message, "Пожалуйста введите команду из списка команд или введите /help")
