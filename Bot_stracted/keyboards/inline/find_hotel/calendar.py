from telebot.types import InlineKeyboardMarkup
from telebot_calendar import Calendar
from datetime import datetime


def markup() -> InlineKeyboardMarkup:
    """Функция создает и возвращает встроенную клавиатуру (календарь)"""
    calendar = Calendar()
    now = datetime.now()
    return calendar.create_calendar(
        name='calendar_1',
        year=now.year,
        month=now.month)
