from loader import bot
from states.find_hotel import FindHotelState
from states.edit import EditStates
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import confirm


@bot.callback_query_handler(state=EditStates.num_of_hotel, func=None)
def num_of_hotel(call: CallbackQuery) -> None:
    """Обработчик для изменения максимального количества отображаемых результатов поиска."""
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['user_data']['num_of_hotel'] = call.data
        bot.set_state(call.from_user.id, FindHotelState.confirm_data_state)
        bot.send_message(call.from_user.id,
                         u'Подтвердите введенные данные \U0001F642',
                         reply_markup=confirm.markup(data['user_data']))
