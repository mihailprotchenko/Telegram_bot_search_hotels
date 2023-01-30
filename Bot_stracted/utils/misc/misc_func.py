from typing import Dict
from utils.misc.caption_maker import caption_maker
from telebot.types import InputMediaPhoto


def insert_img(img: str, caption: Dict) -> InputMediaPhoto(str, str):
    """Функция для формирования фото с описанием, для передачи"""
    return InputMediaPhoto(img, caption_maker(name=caption["name"],
                                              price=caption["price"],
                                              distance_from_center=caption["distance_from_center"],
                                              total_price=caption["distance_from_center"],
                                              site=caption["urls"]))
