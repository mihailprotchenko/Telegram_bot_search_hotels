from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.misc.rapid_api import city
from typing import Tuple, List, Dict, Union


def markup(city_name: str) -> Union[Tuple[InlineKeyboardMarkup, List[Dict]], Tuple[None, None]]:
    """Функция принимает на вход название города, создает и возвращает встроенную клавиатуру
    в которой кнопки формируется из найденных регионов города, а так же список найденных регионов города
    при этом каждой кнопка возвращает строку содержащую id выбранного района"""
    result = city.find(city_name)
    if result:
        destinations = InlineKeyboardMarkup()
        regions = dict()
        for region in result:
            destinations.add(InlineKeyboardButton(text=region['region_name'],
                                                  callback_data=region['destination_id']))
            regions[region['destination_id']] = region['region_name']
        return destinations, regions
    else:
        return None, None
