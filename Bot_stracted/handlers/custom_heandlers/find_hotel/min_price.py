from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import Message


@bot.message_handler(state=FindHotelState.min_price_state)
def min_price(message: Message) -> None:
    """Обработчик для минимальной цены за ночь в отеле"""
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if message.text.isdigit():
            bot.delete_message(chat_id=message.chat.id, message_id=data['message_to_del'])
            data['user_data']['min_price'] = message.text
            bot.set_state(message.from_user.id, FindHotelState.max_price_state)
            data['message_to_del'] = bot.send_message(message.from_user.id,
                                                      u'Введите максимальную стоимость проживания за ночь\U0001F4B5').id

        else:
            data['message_to_del'] = bot.send_message(message.from_user.id,
                                                      u'Вы ввели некорректную сумму, попробуйте еще раз\U0001F605').id
