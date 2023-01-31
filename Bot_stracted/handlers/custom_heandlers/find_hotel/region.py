from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import num_of_hotel


@bot.callback_query_handler(state=FindHotelState.neighborhood_state, func=None)
def choose_region(call: CallbackQuery) -> None:
    """Обработчик для кнопки выбора района, вызывает встроенную клавиатуру, с помощью которой боту передается информация
    о количестве выдаваемых результатов поиска (10, 15, 25 результатов).
    Передает боту id района, который был выбран пользователем"""
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['user_data']['region'] = data['api_data']['regions'].get(call.data, 0)
        data['api_data']['destinationId'] = call.data
        if data['user_data']['filter'] == 'DISTANCE_FROM_LANDMARK':
            bot.set_state(call.from_user.id, FindHotelState.min_price_state)
            data['message_to_del'] = bot.send_message(call.from_user.id,
                                                      u"Введите минимальную стоимость проживания за ночь\U0001F4B5").id
        else:
            data['user_data']['min_price'] = None
            data['user_data']['max_price'] = None
            bot.set_state(call.from_user.id, FindHotelState.num_of_hotel_state)
            bot.send_message(call.from_user.id,
                             u"Сколько отелей показать?\U0001F3E8", reply_markup=num_of_hotel.markup())
