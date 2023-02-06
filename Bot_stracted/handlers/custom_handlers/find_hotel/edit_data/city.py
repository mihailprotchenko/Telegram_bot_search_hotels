from loader import bot
from states.edit import EditStates
from keyboards.inline.find_hotel import region
from telebot.types import Message


@bot.message_handler(state=EditStates.city_state, func=None)
def start_lowprice(message: Message) -> None:
    """Обработчик для изменения введенного города
    Если город найден вызывает клавиатуру с найденными районами города"""
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        bot.delete_message(chat_id=message.chat.id, message_id=data['message_to_del'])
        result, regions = region.markup(message.text)
        if result:
            data['user_data']['city'] = message.text
            data['api_data']['regions'] = regions
            bot.set_state(message.from_user.id, EditStates.neighborhood_state)
            bot.send_message(message.from_user.id, u'Выберите район города \U0001F3D9',
                             reply_markup=result)
        else:
            data['message_to_del'] = bot.send_message(message.from_user.id, u'Город не найден.\U0001F605').id
