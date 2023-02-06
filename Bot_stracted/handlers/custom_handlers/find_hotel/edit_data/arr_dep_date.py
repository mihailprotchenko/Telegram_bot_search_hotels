from loader import bot
from states.find_hotel import FindHotelState
from states.edit import EditStates
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import calendar, confirm
from telebot_calendar import CallbackData, Calendar


user_calendar = Calendar()
calendar_callbackdata = CallbackData("calendar_1", "action", "year", "month", "day")


@bot.callback_query_handler(state=EditStates.arrival_date_state, func=None)
def choose_arrival_date(call: CallbackQuery) -> None:
    """Обработчик для изменения дата заселение"""
    (name, action, year, month, day) = call.data.split(calendar_callbackdata.sep)
    date = user_calendar.calendar_query_handler(bot=bot, call=call, name=name,
                                                action=action, year=year, month=month, day=day)
    if call.data.startswith('calendar_1:DAY'):
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            delta_date = data['api_data']['checkOut'] - date
            # проверка корректности введенных дат
            if delta_date.days > 0:
                data['api_data']['checkIn'] = date
                data['user_data']['format_checkIn'] = date.strftime('%Y-%m-%d')
                bot.set_state(call.from_user.id, FindHotelState.confirm_data_state)
                bot.send_message(call.from_user.id,
                                 u'Подтвердите введенные данные \U0001F642',
                                 reply_markup=confirm.markup(data['user_data']))
            else:
                bot.send_message(call.from_user.id, u"Некорректная дата прибытия/убытия. Попробуйте снова.\U0001F605",
                                 reply_markup=calendar.markup())


@bot.callback_query_handler(state=EditStates.departures_date_state, func=None)
def choose_arrival_date(call: CallbackQuery) -> None:
    """Обработчик для даты выселения"""
    (name, action, year, month, day) = call.data.split(calendar_callbackdata.sep)
    date = user_calendar.calendar_query_handler(bot=bot, call=call, name=name,
                                                action=action, year=year, month=month, day=day)
    if call.data.startswith('calendar_1:DAY'):
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            delta_date = date - data['api_data']['checkIn']
            # проверка корректности введенных дат
            if delta_date.days > 0:
                data['api_data']['checkOut'] = date
                data['user_data']['format_checkOut'] = date.strftime('%Y-%m-%d')
                bot.set_state(call.from_user.id, FindHotelState.confirm_data_state)
                bot.send_message(call.from_user.id,
                                 u'Подтвердите введенные данные \U0001F642',
                                 reply_markup=confirm.markup(data['user_data']))
            else:
                bot.send_message(call.from_user.id, u"Некорректная дата прибытия/убытия. Попробуйте снова.\U0001F605",
                                 reply_markup=calendar.markup())
