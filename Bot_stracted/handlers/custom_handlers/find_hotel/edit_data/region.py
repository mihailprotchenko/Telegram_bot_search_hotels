from loader import bot
from states.find_hotel import FindHotelState
from states.edit import EditStates
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import confirm


@bot.callback_query_handler(state=EditStates.neighborhood_state, func=None)
def find_city(call: CallbackQuery) -> None:
    """Обработчик для изменения выбранного региона."""
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        for reg in data['api_data']['regions']:
            if reg.get('destination_id', 0) == call.data:
                data['user_data']['region'] = reg.get('region_name', 0)
                break
        data['api_data']['destinationId'] = call.data
        bot.set_state(call.from_user.id, FindHotelState.confirm_data_state)
        bot.send_message(call.from_user.id,
                         u'Подтвердите введенные данные \U0001F440',
                         reply_markup=confirm.markup(data['user_data']))
