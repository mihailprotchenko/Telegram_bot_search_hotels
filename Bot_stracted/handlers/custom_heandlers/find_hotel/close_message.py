from loader import bot


@bot.callback_query_handler(func=lambda call: call.data == 'close')
def close_message(call):
    """Обработчик для удаления сообщения содержащем информацию об отеле"""
    bot.delete_message(call.message.chat.id, call.message.message_id)
