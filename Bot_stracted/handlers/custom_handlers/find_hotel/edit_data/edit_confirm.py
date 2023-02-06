from loader import bot
from states.find_hotel import FindHotelState
from states.edit import EditStates
from telebot.types import CallbackQuery
from keyboards.inline.find_hotel import calendar, num_of_hotel, region, num_of_upload_img, upload_image


@bot.callback_query_handler(state=FindHotelState.confirm_data_state, func=None)
def edit(call: CallbackQuery) -> None:
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        """Обработчик для изменения введенных пользователем данных."""
        if call.data == 'checkin':
            bot.set_state(call.from_user.id, EditStates.arrival_date_state)
            bot.send_message(call.from_user.id, "Выберите дату заселения",
                             reply_markup=calendar.markup())
        elif call.data == 'checkin':
            bot.set_state(call.from_user.id, EditStates.departures_date_state)
            bot.send_message(call.from_user.id, "Выберите дату выселения",
                             reply_markup=calendar.markup())
        elif call.data == 'city':
            data['message_to_del'] = bot.send_message(call.from_user.id, 'В какой город вы хотите отправиться?').id
            bot.set_state(call.from_user.id, EditStates.city_state)
        elif call.data == 'num_of_hotel':
            """Обработчик для кнопки отображения количества результатов."""
            bot.set_state(call.from_user.id, EditStates.num_of_hotel)
            bot.send_message(call.from_user.id, u"Сколько отелей показать?\U0001F3E8",
                             reply_markup=num_of_hotel.markup())
        elif call.data == 'region':
            result = region.markup(data['user_data']['city'])
            bot.set_state(call.from_user.id, EditStates.neighborhood_state)
            bot.send_message(call.from_user.id, 'Измените район города (щелкнув по кнопке)',
                             reply_markup=result)
        elif call.data == 'photo':
            bot.set_state(call.from_user.id, EditStates.load_photos_state)
            bot.send_message(call.from_user.id, u"Нужно ли загружать картинки?\U0001F3B4",
                             reply_markup=upload_image.markup())
        elif call.data == 'photo_num':
            bot.set_state(call.from_user.id, EditStates.num_of_photos_state)
            bot.send_message(call.from_user.id, u"Сколько фото каждого отеля загрузить?\U0001F3B4",
                             reply_markup=num_of_upload_img.markup())
        elif call.data == 'min_price':
            bot.set_state(call.from_user.id, EditStates.min_price_state)
            data['message_to_del'] = bot.send_message(call.from_user.id, u"Введите минимальную "
                                                                         u"стоимость проживания за ночь\U0001F4B5").id
        elif call.data == 'max_price':
            bot.set_state(call.from_user.id, EditStates.max_price_state)
            data['message_to_del'] = bot.send_message(call.from_user.id, u"Введите максимальную "
                                                                         u"стоимость проживания за ночь\U0001F4B5").id
