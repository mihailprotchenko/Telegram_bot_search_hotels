from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def markup() -> InlineKeyboardMarkup:
    """Функция создает и возвращает встроенную клавиатуру, в которой кнопками передается информация о том,
    сколько нужно выводить пользователю фотографии отеля"""
    num_upl_img = InlineKeyboardMarkup()
    num_upl_img.add(InlineKeyboardButton(text='1', callback_data=1),
                    InlineKeyboardButton(text='3', callback_data=3),
                    InlineKeyboardButton(text='5', callback_data=5))
    return num_upl_img
