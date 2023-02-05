from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def markup() -> InlineKeyboardMarkup:
    """Функция создает и возвращает встроенную клавиатуру, в которой кнопками передается информация о том,
    нужно ли выводить пользователю фотографии отеля"""
    upl_img = InlineKeyboardMarkup()
    upl_img.add(InlineKeyboardButton(text='Да', callback_data='Yes'),
                InlineKeyboardButton(text='Нет', callback_data='No'))
    return upl_img
