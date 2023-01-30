from typing import Tuple
from utils.misc.rapid_api import request
import json
import re


def find(hotel_id: str, num_of_photo: int) -> Tuple:
    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
    querystring = {"id": hotel_id}
    response = request.create(url=url, querystring=querystring)
    pattern = re.compile(r'"hotelImages"')
    print(response.text)
    if response and pattern.search(response.text):
        found_hotel_images = json.loads(response.text).get('hotelImages', 0)
        hotel_img = [re.sub(r'(?<=\w)/(?=\w)', '//', re.sub(r'{size}', 'l', image.get('baseUrl', 0)))
                     for image in found_hotel_images[:num_of_photo + 1]]
    else:
        hotel_img = [open('./No_image.jpg', 'rb')]
    return tuple(hotel_img)
