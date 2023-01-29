import handlers
from loader import bot
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands
from database.db_create import initialize_db


if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    initialize_db()
    set_default_commands(bot)
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
