from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def markup() -> InlineKeyboardMarkup:
    """Функция создает и возвращает встроенную клавиатуру, в которой кнопками передается информация о том,
     какое количество выводимых отелей из найденного списка отелей отобразить для пользователя."""
    num_of_hotel = InlineKeyboardMarkup()
    num_of_hotel.add(InlineKeyboardButton(text='10', callback_data=10),
                     InlineKeyboardButton(text='15', callback_data=15),
                     InlineKeyboardButton(text='25', callback_data=25))
    return num_of_hotel
