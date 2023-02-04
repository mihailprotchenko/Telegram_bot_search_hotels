from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import CallbackQuery
from utils.misc.rapid_api import hotel
from utils.misc.caption_maker import caption_maker
from database.db_create import RequestData, ResponseData, db


@bot.callback_query_handler(state=FindHotelState.confirm_data_state, func=lambda call: call.data == 'start')
def choose_departures_date(call: CallbackQuery) -> None:
    """Обработчик для подтверждения о введенных пользователем данных.
    Вызывается если выбрана загрузка результатов без фотографий отелей"""
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        user_data = data['user_data']
        hotels_found = hotel.find(data['api_data']['destinationId'],
                                  user_data['num_of_hotel'],
                                  user_data['format_checkIn'],
                                  user_data['format_checkOut'],
                                  user_data['delta_date'],
                                  user_data['filter'],
                                  user_data['min_price'],
                                  user_data['max_price'])
        #  Если отели найдены, то отправляет краткая информация о каждом
        #  Так же в таблицы RequestData, ResponseData, базы данных вносится информация введенная пользователем,
        #  информация об отелях, фотографии отелей, полученные от rapid_api соответственно.
    if hotels_found:
        with db:
            req = RequestData.create(user_id=call.from_user.id,
                                     command=user_data['command'],
                                     chat_id=call.message.chat.id,
                                     city=user_data['city'],
                                     region=user_data['region'],
                                     num_of_hotel=user_data['num_of_hotel'],
                                     load_photo='Нет',
                                     amount_photo=user_data['pic_to_upload'],
                                     arrival_date=user_data['format_checkIn'],
                                     departures_date=user_data['format_checkOut'],
                                     min_price=user_data['min_price'],
                                     max_price=user_data['max_price'])
        bot.set_state(call.from_user.id, FindHotelState.send_result_state)
        for el in hotels_found:
            # уведомляем пользователя об обработке полученных данных
            bot.send_chat_action(call.message.chat.id, action='typing')
            with db:
                ResponseData.create(request_id=req.id,
                                    hotel_id=el['id'],
                                    name=el['name'],
                                    distance_from_center=el['distance_from_center'],
                                    price=el['urls'],
                                    total_price=el["total_price"],
                                    url=el["urls"])
            bot.send_message(call.from_user.id,
                             caption_maker(el["name"], el["price"], el["total_price"],
                                           el["distance_from_center"], el["urls"]))
    else:
        bot.send_message(call.from_user.id, 'Отели не найдены.')
        bot.set_state(call.from_user.id, None)
