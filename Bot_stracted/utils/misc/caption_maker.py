def caption_maker(name: str, price: str, total_price: str, distance_from_center: str, site: str):
    return f'Название: {name}'\
         f'\nЦена за ночь: {price}'\
         f'\nЦена за выбранный период: {total_price}$'\
         f'\nРасстояние до центра: {distance_from_center}'\
         f'\nСайт: {site}'
