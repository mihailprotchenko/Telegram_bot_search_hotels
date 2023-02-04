from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import calendar


@bot.callback_query_handler(state=FindHotelState.num_of_photos_state, func=None)
def photo_amount(call: CallbackQuery) -> None:
    """Обработчик для кнопки отвечающей за количество загружаемых фотографий отелей."""
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['user_data']['pic_to_upload'] = int(call.data) - 1
        bot.set_state(call.from_user.id, FindHotelState.arrival_date_state)
        bot.send_message(call.from_user.id,
                         u"Выберите дату заселения \U0001F6EC",
                         reply_markup=calendar.markup())
