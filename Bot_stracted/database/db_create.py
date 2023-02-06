from peewee import *

db = SqliteDatabase('./database/bot_db.db')


class BaseModel(Model):
    class Meta:
        database = db


class RequestData(BaseModel):  # таблица хранящая все данные которые ввел пользователь для формирования поискового запроса
    id = UUIDField.auto_increment  # id строки
    user_id = IntegerField()  # id юзера вводившего данные
    command = CharField()  #
    chat_id = IntegerField()  # id чата из которого были получены данные
    city = CharField()  # название города
    region = CharField()  # название региона
    num_of_hotel = IntegerField()  # количество результатов поиска
    load_photo = CharField()  # загрузка фотографий(да/нет)
    amount_photo = IntegerField(null=True)  # количество загружаемых фотографий
    arrival_date = DateField()  # дата прибытия
    departures_date = DateField()  # дата выселения
    min_price = IntegerField(null=True)  # минимальная цена за ночь
    max_price = IntegerField(null=True)  # максимальная цена за ночь


class ResponseData(BaseModel):  # таблица хранящая данные полученный от rapidapi
    id = UUIDField.auto_increment  # id строки
    request_id = ForeignKeyField(RequestData.id, backref='response')  # внешний ключ из таблицы RequestData (id реквеста)
    hotel_id = IntegerField()  # id отеля
    name = CharField()  # название отеля
    distance_from_center = CharField()  # расстояние до центра
    price = CharField()  # цена за ночь для одного взрослого
    total_price = CharField()  # цена за выбранный срок проживания
    url = TextField()  # ссылка на сайт отеля


class Photos(BaseModel):  # таблица хранящая фотографии отелей полученное от rapidapi
    id = UUIDField.auto_increment  # id фотографии
    hotel_id = ForeignKeyField(ResponseData.hotel_id)  # внешний ключ из таблицы ResponseData (id отеля)
    photo = CharField()  # ссылка на фотографию отеля


def initialize_db():  # функция создает подключение к базе, если таблицы не созданы, то создает их
    db.connect()
    db.create_tables([RequestData, ResponseData, Photos], safe=True)
    db.close()
