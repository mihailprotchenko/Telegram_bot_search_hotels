from telebot.types import Message
from states.history import HistoryStates
from loader import bot
from database.db_create import RequestData, ResponseData, Photos, db
from keyboards.inline.find_hotel import photos_slider
from utils.misc.caption_maker import caption_maker
from utils.misc.misc_func import insert_img


@bot.message_handler(commands=['history'])
def retrieve(message: Message):
    """Обработчик для команды /history, создает запрос к базе, где по telegram_id пользователя, находит все созданные им
    запросы. Отправляет сообщение содержащие параметры поискового запроса. Затем находит в таблице ResponseData
     соответсвующее RequestData.id записи и отправляет их пользователю. При этом если пользователь выбрал загружать
     фото отелей при формировании запроса, то из таблицы Photos выбираются строки с совпадающим hotel_id"""
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    bot.send_message(message.chat.id, 'Результаты ваших поисковых запросов:')
    with db:
        for el in RequestData.select().where(RequestData.user_id == message.from_user.id).limit(5):
            bot.send_message(message.chat.id,
                             'Команда: {command}\n'
                             'Город: {city}\n'
                             'Район: {region}\n'
                             'Количество выводимых результатов: {num_of_hotel}\n'
                             'Загрузка фотографий: {load_photo}\n'
                             '{amount_photo}'
                             'Дата прибытия: {arrival_date}\n'
                             'Дата выселения: {departures_date}\n'
                             '{min_price}'
                             '{max_price}'.format(
                                                   command=el.command, city=el.city, region=el.region,
                                                   num_of_hotel=el.num_of_hotel,
                                                   load_photo=el.load_photo,
                                                   amount_photo=f'Количество фотографий:{el.amount_photo + 1}\n'
                                                   if el.load_photo == 'Да'
                                                   else '',
                                                   arrival_date=el.arrival_date,
                                                   departures_date=el.departures_date,
                                                   min_price=f'Минимальная цена: {el.min_price}\n'
                                                   if el.min_price else '',
                                                   max_price=f'Максимальная цена: {el.max_price}'
                                                   if el.max_price else ''))
            for hotel in ResponseData.select().where(ResponseData.request_id == el.id):
                caption = caption_maker(hotel.name, hotel.price, hotel.total_price, hotel.distance_from_center, hotel.url)
                if el.load_photo == 'Да':
                    bot.set_state(message.from_user.id, HistoryStates.result_with_pic_state)
                    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                        with db:
                            data[f"images_of_{hotel.hotel_id}"] = \
                                [url.photo for url in Photos.select().where(Photos.hotel_id == hotel.hotel_id)]
                        data[f"caption_of_{hotel.hotel_id}"] = caption
                        try:
                            bot.send_photo(message.from_user.id,
                                           photo=data[f"images_of_{hotel.hotel_id}"][0],
                                           caption=data[f"caption_of_{hotel.hotel_id}"],
                                           reply_markup=photos_slider.markup(len(data[f"images_of_{hotel.hotel_id}"]),
                                                                             hotel.hotel_id))
                        except IndexError:
                            bot.send_photo(message.from_user.id, photo=open('./No_image.jpg', 'rb'),
                                           caption=caption)

                else:
                    bot.send_message(message.from_user.id, caption)
