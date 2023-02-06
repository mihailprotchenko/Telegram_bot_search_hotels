from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import calendar, confirm
from telebot_calendar import CallbackData, Calendar


@bot.callback_query_handler(state=FindHotelState.departures_date_state, func=None)
def choose_departures_date(call: CallbackQuery) -> None:
    """Обработчик для календаря (дата выселения)"""
    departures_calendar = Calendar()
    calendar_callbackdata = CallbackData("calendar_1", "action", "year", "month", "day")
    (name, action, year, month, day) = call.data.split(calendar_callbackdata.sep)
    date = departures_calendar.calendar_query_handler(bot=bot, call=call, name=name,
                                                      action=action, year=year, month=month, day=day)
    if call.data.startswith('calendar_1:DAY'):
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data['api_data']['checkOut'] = date
            data['user_data']['format_checkOut'] = date.strftime('%Y-%m-%d')
            delta_date = data['api_data']['checkOut'] - data['api_data']['checkIn']
            # проверка корректности введенных дат
            # если данные введены верно, то просит пользователя подтвердить введенные данные или изменить их
            if delta_date.days > 0:
                data['user_data']['delta_date'] = delta_date.days
                bot.set_state(call.from_user.id, FindHotelState.confirm_data_state)
                bot.send_message(call.from_user.id,
                                 u'Подтвердите либо измените введенные данные \U0001F440',
                                 reply_markup=confirm.markup(data['user_data']))

            else:
                bot.set_state(call.from_user.id, FindHotelState.arrival_date_state)
                bot.send_message(call.from_user.id, u"Некорректная дата прибытия/убытия. Попробуйте снова.\U0001F605",
                                 reply_markup=calendar.markup())
