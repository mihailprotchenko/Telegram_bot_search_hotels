from states.edit import EditStates
from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import Message
from keyboards.inline.find_hotel import confirm
from telebot.apihelper import ApiTelegramException


@bot.message_handler(state=EditStates.min_price_state, func=None)
def min_price(message: Message) -> None:
    """Обработчик для изменения минимальной цены номера за ночь"""
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        try:
            #  Если пользователь, уже ввел некорректные данные, то удаляет предупреждение бота об этом.
            #  Если сообщение не было, то обрабатывает исключение ApiTelegramException.
            bot.delete_message(chat_id=message.chat.id, message_id=data['message_to_del'])
        except ApiTelegramException:
            print("message didn't exists")
        finally:
            try:
                #  Проверяет корректность введенных данных.
                # Если данные не корректны (передано не число или, минимальная цена больше максимальной, то
                # поднимает исключение ValueError и обрабатывает его выводом сообщение пользователю
                if int(message.text) < int(data['user_data']['max_price']):
                    data['user_data']['min_price'] = message.text
                    bot.set_state(message.from_user.id, FindHotelState.confirm_data_state)
                    bot.send_message(message.from_user.id, u'Подтвердите введенные данные \U0001F642',
                                     reply_markup=confirm.markup(data['user_data']))
                else:
                    raise ValueError
            except ValueError:
                data['message_to_del'] = bot.send_message(message.from_user.id,
                                                          u'Вы ввели некорректную сумму, '
                                                          u'попробуйте еще раз\U0001F605').id


@bot.message_handler(state=EditStates.max_price_state, func=None)
def max_price(message: Message) -> None:
    """Обработчик для изменения максимальной цены номера за ночь"""
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        try:
            #  Если пользователь, уже ввел некорректные данные, то удаляет предупреждение бота об этом.
            #  Если сообщение не было, то обрабатывает исключение ApiTelegramException.
            bot.delete_message(chat_id=message.chat.id, message_id=data['message_to_del'])
        except ApiTelegramException:
            print("message didn't exists")
        finally:
            try:
                #  Проверяет корректность введенных данных.
                # Если данные не корректны (передано не число или, минимальная цена больше максимальной, то
                # поднимает исключение ValueError и обрабатывает его выводом сообщение пользователю
                if int(message.text) > int(data['user_data']['min_price']):
                    data['user_data']['max_price'] = message.text
                    bot.set_state(message.from_user.id, FindHotelState.confirm_data_state)
                    bot.send_message(message.from_user.id, u'Подтвердите введенные данные \U0001F642',
                                     reply_markup=confirm.markup(data['user_data']))
                else:
                    raise ValueError
            except ValueError:
                data['message_to_del'] = bot.send_message(message.from_user.id,
                                                          u'Вы ввели некорректную сумму, '
                                                          u'попробуйте еще раз\U0001F605').id
