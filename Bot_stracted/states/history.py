from telebot.handler_backends import State, StatesGroup


class HistoryStates(StatesGroup):
    #  Класс описывающий состояние пользователя в контексте отправки истории поиска
    result_with_pic_state = State()  # отправка данных об отелях полученных из БД пользователю
