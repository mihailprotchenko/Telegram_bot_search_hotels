from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import Message
from keyboards.inline.find_hotel import num_of_hotel


@bot.message_handler(state=FindHotelState.max_price_state)
def max_price(message: Message) -> None:
    """Обработчик для максимальной цены за ночь в отеле"""
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if message.text.isdigit():
            bot.delete_message(chat_id=message.chat.id, message_id=data['message_to_del'])
            if int(data['user_data']['min_price']) < int(message.text):
                data['user_data']['max_price'] = message.text
                bot.set_state(message.from_user.id, FindHotelState.num_of_hotel_state)
                bot.send_message(message.from_user.id,
                                 u"Сколько отелей показать?\U0001F3E8",
                                 reply_markup=num_of_hotel.markup())
            else:
                data['message_to_del'] = bot.send_message(message.from_user.id,
                                                          u'Минимальная сумма больше максимальной\U0001F605. '
                                                          u'Введите минимальную стоимость проживания.\U0001F4B5').id
                bot.set_state(message.from_user.id, FindHotelState.min_price_state)

        else:
            data['message_to_del'] = bot.send_message(message.from_user.id,
                                                      u'Вы ввели некорректную сумму. Попробуйте еще раз\U0001F605').id
