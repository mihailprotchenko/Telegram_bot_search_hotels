from utils.misc.rapid_api import request
from typing import List, Dict
import json
import re


def find(city_name: str) -> List[Dict]:
    """Функция поиска районов для заданного города.
    Возвращает список состоящий словарей, которые содержат информацию о найденных районах города
     (название района ('region_name'), id региона для дальнейшего поиска отелей в нем('destination_id')).
    Формируем данные для запроса к api hotels:
    url по которому будем обращаться, название города (query), language code (locale), валюту в которой
     будет рассчитываться цена (currency)"""
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"
    querystring = {"query": city_name, "locale": "ru_RU", "currency": "USD"}
    """Проверяем содержит ли полученный json-файл нужные нам данный о районах города, если нет, то возвращаем пустой 
    список районов. Если файл содержит нужную информацию то десериализуем его, ищем в нем данные для дальнейшего 
    формирования запросов к API Hotels и вывода для юзера ('region_name', 'destination_id'), если в процессе поиска
     произошло исключение AttributeError (полученная структура не соответствует той, в которой мы должны искать данные) 
     обрабатываем """
    response = request.create(url=url, querystring=querystring)
    if response:
        pattern = re.compile(r'(?<=\"CITY_GROUP\",).+?[\]]')
        if pattern.search(response.text):
            try:
                for elem in json.loads(response.text).get("suggestions", 0):
                    if elem.get("group", 0) == "CITY_GROUP":
                        city_group = ({'region_name': re.sub(r'(\<(/?[^>]+)>)', '', region.get('caption', 0)),
                                           'destination_id': region.get('destinationId', 0)} for region in elem.get('entities', 0))
                        break
            except AttributeError:
                print('City response data error.')
            return city_group
