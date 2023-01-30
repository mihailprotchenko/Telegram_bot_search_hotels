from telebot.handler_backends import State, StatesGroup


class EditStates(StatesGroup):
    # Класс описывающий состояние пользователя при изменении введенных им до этого данных
    city_state = State()  # ввод города
    neighborhood_state = State()  # выбор района
    min_price_state = State()  # ввод минимальной цены
    max_price_state = State()  # ввод максимальной цены
    num_of_hotel = State()  # выбор количества результатов поиска
    load_photos_state = State()  # выбор загрузки фотографий отелей
    num_of_photos_state = State()  # выбор количества загружаемых фотографий отелей
    arrival_date_state = State()  # выбор даты прибытия
    departures_date_state = State()  # выбор даты убытия
