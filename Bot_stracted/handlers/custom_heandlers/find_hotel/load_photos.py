from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import calendar, num_of_upload_img


@bot.callback_query_handler(state=FindHotelState.load_photos_state, func=None)
def load_photos(call: CallbackQuery) -> None:
    """Обработчик для кнопки отображения фото отелей. Вызывает встроенну клавиатуру для выбора даты заселения или
    количества загружаемых фотографий отелей"""
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['user_data']['upload_image'] = call.data
        if call.data == 'Yes':
            bot.set_state(call.from_user.id, FindHotelState.num_of_photos_state)
            bot.send_message(call.from_user.id, u"Сколько фото каждого отеля загрузить?\U0001F3B4",
                             reply_markup=num_of_upload_img.markup())
        else:
            bot.set_state(call.from_user.id, FindHotelState.arrival_date_state)
            data['user_data']['pic_to_upload'] = 0
            bot.send_message(call.from_user.id, u"Выберите дату заселения\U0001F6EC",
                             reply_markup=calendar.markup())
