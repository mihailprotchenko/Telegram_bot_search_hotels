import requests
from typing import Dict, Union
from requests import Response, Timeout
from config_data.config import RAPID_API_KEY, RAPID_API_HOST


def create(url: str, querystring: Dict) -> Union[Response, None]:
    """Формируем запрос для api hotels в котором указываем url запроса(url),
     заголовки (headers) и параметры (querystring), а так же ключ для обращения к api (x-rapidapi-key)
        и url по которому мы будем обращаться к хосту api (x-rapidapi-host).
        Если мы получаем статус код 200 то, возвращаем полученные данные иначе ничего не возвращаем"""
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_HOST
    }
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        if response.status_code == 200:
            return response
    except Timeout:
        return
