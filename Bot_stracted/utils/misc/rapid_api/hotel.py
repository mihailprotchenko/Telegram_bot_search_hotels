from typing import Dict, Union, Any, Generator
from utils.misc.rapid_api import request
import json
import re


def find(destination_id: str, pagesize: str, checkIn: str, checkOut: str, delta_time: int, sort_type: str,
         price_min: str = None, price_max: str = None) -> Generator[Dict[str, Union[Union[str, int], Any]], Any, None]:
    """Функция получается на вход id района, в котором нужно найти отели (destination_id),
    количество отелей которые нужно отправить пользователю (pagesize), дата заселения в отель (checkIn), дату выселения
     из отеля (checkOut), количество дней пребывания, а так же тип сортировки.
    Возвращает список состоящий из словарей, в которых указана информация о найденных отелях:
    Названия отеля ('name'), цена за ночь одного взрослого('price'), количество звезд('info'), а
    так же фото из отеля('image')

    Формируем запрос для api hotels в котором указываем url запроса(url),
    id района по которому будет производиться поиск отелей (destinationId), количество отображаемых результатов поиска
    (pageSize), дата заселения в отель (checkIn), дата выселения из отеля (checkOut), количество взрослых (adults1),
    сортировку по которой будут выводиться отели(sortOrder), язык на котором будут выводиться результаты поиска (locale),
    информация в какой валюте рассчитывать цены (currency)."""
    url = "https://hotels4.p.rapidapi.com/properties/list"
    querystring = {"destinationId": destination_id, "pageNumber": "1", "pageSize": pagesize, "checkIn": checkIn,
                   "checkOut": checkOut, "adults1": "1", "sortOrder": sort_type, "locale": "ru_RU",
                   "currency": "USD", "priceMin": price_min, "priceMax": price_max}
    response = request.create(url=url, querystring=querystring)
    if response:
        pattern = re.compile(r'(?<="results":).+}}]')
        """Проверяем содержит ли полученный json-файл нужные нам данный о районах города, если нет, то возвращаем пустой 
            список отелей. Если файл содержит нужную информацию то десериализуем его и формируем из
             полученных данных список, содержащий словари, в которых отражена краткая информация об
             отеле для пользователя.Если в процессе поиска произошло исключение AttributeError
              (полученная структура не соответствует той, в которой мы должны искать данные) 
             обрабатываем """
        if pattern.search(response.text):
            try:
                found_hotels = json.loads(response.text).get('data', 0).get('body', 0).get('searchResults', 0) \
                    .get('results', 0)
                hotels_with_short_info = ({'id': hotel.get('id', 0),
                     'name': hotel.get('name', 0),
                     'price': hotel.get('ratePlan', 0).get('price', 0).get('current', 0),
                     'total_price': int(hotel.get('ratePlan', 0).get('price', 0).get('exactCurrent', 0)) * delta_time,
                     'distance_from_center': hotel.get('landmarks', 0)[0].get('distance', 0),
                     'urls': f"https://www.hotels.com/ho{hotel.get('id', 0)}",
                     } for hotel in found_hotels)
            except (AttributeError, ValueError):
                print('Hotel response data error.')
            return hotels_with_short_info
