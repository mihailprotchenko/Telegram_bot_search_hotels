from loader import bot
from states.find_hotel import FindHotelState
from keyboards.inline.find_hotel import region
from telebot.types import Message


@bot.message_handler(state=FindHotelState.city_state, func=lambda message: not message.text.startswith('/'))
def find_city(message: Message) -> None:
    """Обработчик для введенного пользователем города"""
    result, regions = region.markup(message.text)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if result:
            bot.delete_message(chat_id=message.chat.id, message_id=data['message_to_del'])
            data['api_data'] = {}
            data['user_data']['city'] = message.text
            data['api_data']['regions'] = regions
            bot.set_state(message.from_user.id, FindHotelState.neighborhood_state)
            bot.send_message(message.from_user.id, u'Выберите район города \U0001F3D9',
                             reply_markup=result)
        else:
            data['message_to_del'] = bot.send_message(message.from_user.id, u'Город не найден.\U0001F605').id
