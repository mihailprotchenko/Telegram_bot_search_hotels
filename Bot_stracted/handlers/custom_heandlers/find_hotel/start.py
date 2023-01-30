from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import Message


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def start_lowprice(message: Message) -> None:
    """Обработчик для команд '/lowprice','/highprice', '/bestdeal', после ввода команды выставляет
    у бота состояние 'LowPriceState.city', а затем отправляет ему сообщение"""
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    bot.set_state(message.from_user.id, FindHotelState.city_state)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if message.text == '/lowprice':
            data['user_data'] = {'filter': 'PRICE'}
        elif message.text == '/highprice':
            data['user_data'] = {'filter': 'PRICE_HIGHEST_FIRST'}
        else:
            data['user_data'] = {'filter': 'DISTANCE_FROM_LANDMARK'}
        data['user_data']['command'] = message.text
        data['message_to_del'] = bot.send_message(message.from_user.id,
                                                  u'В какой город вы хотите отправиться?\U0001F3D9').id
