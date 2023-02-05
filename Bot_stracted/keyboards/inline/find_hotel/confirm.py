from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Dict


def markup(user_data: Dict) -> InlineKeyboardMarkup:
    """"""
    confirm_keyboard = InlineKeyboardMarkup(row_width=1)
    confirm_keyboard.add(
        InlineKeyboardButton(text=u'Город\U0001F3D9:' + f'{user_data["city"]}',
                             callback_data='city'),
        InlineKeyboardButton(text=u'Район\U0001F4CD:' + f'\n{user_data["region"]}',
                             callback_data='region'),
        InlineKeyboardButton(text=u'Количество результатов\U0001F575:' + f'{user_data["num_of_hotel"]}',
                             callback_data='num_of_hotel'),
        InlineKeyboardButton(text=u'Дата прибытия\U0001F6EC:' + f'{user_data["format_checkIn"]}',
                             callback_data='checkin'),
        InlineKeyboardButton(text=u'Дата отъезда\U00002708:' + f'{user_data["format_checkOut"]}',
                             callback_data='checkout'),
        InlineKeyboardButton(text=u'Загрузка фотографий отелей\U0001F5BC:' + f'{user_data["upload_image"]}',
                             callback_data='photo'))
    if user_data['filter'] == 'DISTANCE_FROM_LANDMARK':
        confirm_keyboard.add(
            InlineKeyboardButton(text=u'Мин-ая стоимость за ночь\U0001F4B8:' + f'{user_data["min_price"]}',
                                 callback_data='min_price'),
            InlineKeyboardButton(text=u'Макс-ая стоимость за ночь\U0001F4B8:' + f'{user_data["max_price"]}',
                                 callback_data='max_price'))
    if user_data['upload_image'] == 'Yes':
        confirm_keyboard.add(
            InlineKeyboardButton(text=u'Количество фотографий для загрузки\U0001F5BC:' + f'{user_data["pic_to_upload"] + 1}',
                                 callback_data='photo_num'),
            InlineKeyboardButton(text=u'Подтвердить\U0001F44C',
                                 callback_data='start_with_pic'))
    else:
        confirm_keyboard.add(InlineKeyboardButton(text=u'Подтвердить\U0001F44C',
                                                  callback_data='start',
                                                  parse_mode='HTML'))

    return confirm_keyboard
