from telebot.handler_backends import State, StatesGroup


class FindHotelState(StatesGroup):
    # Класс описывающий состояния пользователя при общении с ботом в контексте поиска отелей.
    city_state = State()  # ввод города
    neighborhood_state = State()  # выбор района
    min_price_state = State()  # ввод минимальной цены
    max_price_state = State()  # ввод максимальной цены
    num_of_hotel_state = State()  # выбор количества результатов поиска
    load_photos_state = State()  # выбор загрузки фотографий отелей
    num_of_photos_state = State()  # выбор количества загружаемых фотографий отелей
    arrival_date_state = State()  # выбор даты прибытия
    departures_date_state = State()  # выбор даты убытия
    confirm_data_state = State()  # подтверждение введенных данных
    send_result_state = State()  # отправка результатов без фото
    send_result_with_photo_state = State()  # отправка результатов с фото
