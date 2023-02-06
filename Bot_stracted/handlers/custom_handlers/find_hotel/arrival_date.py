from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import calendar
from telebot_calendar import CallbackData, Calendar


@bot.callback_query_handler(state=FindHotelState.arrival_date_state, func=None)
def choose_arrival_date(call: CallbackQuery) -> None:
    """Обработчик для календаря (дата заселения)"""
    arrival_calendar = Calendar()
    calendar_callbackdata = CallbackData("calendar_1", "action", "year", "month", "day")
    (name, action, year, month, day) = call.data.split(calendar_callbackdata.sep)
    date = arrival_calendar.calendar_query_handler(bot=bot, call=call, name=name,
                                                   action=action, year=year, month=month, day=day)
    if call.data.startswith('calendar_1:DAY'):
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data['api_data']['checkIn'] = date
            data['user_data']['format_checkIn'] = date.strftime('%Y-%m-%d')
            bot.send_message(call.from_user.id, u"Выберите дату выселения \U00002708",
                             reply_markup=calendar.markup())
            bot.set_state(call.from_user.id, FindHotelState.departures_date_state)
