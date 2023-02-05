from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegram_bot_pagination import InlineKeyboardPaginator


def markup(photos_amount, hotelid, page=1):
    # Создаем пагинатор и кнопку закрыть
    if photos_amount > 1:
        paginator = InlineKeyboardPaginator(photos_amount, current_page=page, data_pattern=f'{hotelid}_'+'{page}')
        paginator.add_after(InlineKeyboardButton(text='Закрыть', callback_data='close'))
        return paginator.markup
    else:
        num_of_hotel = InlineKeyboardMarkup()
        num_of_hotel.add(InlineKeyboardButton(text='Закрыть', callback_data='close'))
        return num_of_hotel
