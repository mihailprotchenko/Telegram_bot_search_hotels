from loader import bot
from states.find_hotel import FindHotelState
from states.edit import EditStates
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import confirm, num_of_upload_img


@bot.callback_query_handler(state=EditStates.load_photos_state, func=None)
def load_photos(call: CallbackQuery) -> None:
    """Обработчик для изменения отображения фото отелей."""
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['user_data']['upload_image'] = call.data
    if call.data == 'Yes':
        bot.set_state(call.from_user.id, EditStates.num_of_photos_state)
        bot.send_message(call.from_user.id, u"Сколько фото каждого отеля загрузить?\U0001F3B4",
                         reply_markup=num_of_upload_img.markup())
    else:
        bot.set_state(call.from_user.id, FindHotelState.confirm_data_state)
        bot.send_message(call.from_user.id, u'Подтвердите введенные данные \U0001F642',
                         reply_markup=confirm.markup(data['user_data']))
