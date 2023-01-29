import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_API_HOST = os.getenv('RAPID_API_HOST')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('lowprice', "Вывести список самый дешевых отелей"),
    ('highprice', "Вывести список самый дорогих отелей"),
    ('bestdeal', "Вывести список отелей, наиболее подходящих по цене и расположению от центра"),
    ('history', "Вывести историю результатов поиска отелей")
)
