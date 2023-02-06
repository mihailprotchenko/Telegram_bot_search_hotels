from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import upload_image


@bot.callback_query_handler(state=FindHotelState.num_of_hotel_state, func=None)
def num_of_hotel(call: CallbackQuery) -> None:
    """Обработчик для кнопки максимального количества отображаемых результатов поиска. Вызывает встроенную клавиатуру,
    с помощью которой боту передается информации о потребности в отправке фотографий отеля.
    Передает боту количество выдаваемых результатов поиска"""

    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['user_data']['num_of_hotel'] = call.data
        bot.set_state(call.from_user.id, FindHotelState.load_photos_state)
        bot.send_message(call.from_user.id,
                         u"Нужно ли загружать картинки?\U0001F3B4",
                         reply_markup=upload_image.markup())
