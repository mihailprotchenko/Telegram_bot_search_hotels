
>##  Telegram-бот для анализа сайта Hotels.com и поиска подходящих пользователю отелей
***
Данный скрипт реализует Telegram-бота, который позволяет подобрать пользователю подходящий отель, основываясь на информации
полученной от сайта Hotels.com.


###REQUIREMENTS
***
Описание используемых библиотек:
* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - простая библиотека позволяющий реализовать работу Telegram bot API;
* [python-dotenv](https://github.com/theskumar/python-dotenv) - библиотека позволяет считывать пары ключ : значение из файла .env и устанавливать их как переменные окружения;
* [requests](https://github.com/psf/requests) HTTP библиотека;
* [telebot-calendar](https://github.com/FlymeDllVa/Telebot-Calendar) - календарь для telebot;
* [peewee](https://github.com/coleifer/peewee) - ORM для работы с базой данных;
* [python-telegram-bot-pagination](https://github.com/ksinn/python-telegram-bot-pagination) - позволяет реализовать нумерацию страниц в сообщениях с фотографиями отелей.
  <!---->
Вы так же можете установить требуемые библиотеки описаны из в файле __requirements.txt__ с использованием pip:
>pip install -r requirements.txt


### INSTALLATION
***
Для работы Telegram-бота требуется получить __ключ-бота__, для общения с telegram bot api, а так же __ключ для работы с api сайта Hotels.com__.
+ [Как получить ключ Telegram-бота](https://core.telegram.org/bots#6-botfather)
+ Как получить ключ для работы с api сайта Hotels.com:
  * зарегистрируйтесь на сайте [rapidapi.com](rapidapi.com);
  * перейдите в API Marketplace → категория Travel → Hotels (либо просто перейдите по прямой ссылке на документацию [Hotels API Documentation](https://rapidapi.com/apidojo/api/hotels4/));
  * нажмите кнопку Subscribe to Test;
  * выберите бесплатный пакет (Basic). 
  <!---->
После того как вы получили ключ-бота, а так же ключ для работы с api сайта Hotels.com внесите их в файл <code>.env</code>. Для формирования своего <code>.env</code> файла исползуйте <code>[.env.template](.env.template)</code>

###DOCUMENTATION
***
####FUNCTIONAL:
Бот имеет следующий набор команд:
* __/lowprice__ - Поиск отелей с сортировкой по убыванию цены
* __/highprice__ - Поиск отелей с сортировкой по возрастанию цены
* __/bestdeal__ - Поиск отелей с лучшим соотношением цены/расстояние до центра
* __/history__ - История запросов пользователя(лимит отправляемых запросов - 5)
  <!---->
Алгоритмы команд __/lowprice, /highprice, /bestdeal__:
1. опрос пользователя;
    * [выбор типа сортировки](handlers/custom_handlers/find_hotel/start.py)
    * [город](handlers/custom_handlers/find_hotel/city.py);
    * [район города](handlers/custom_handlers/find_hotel/region.py);
    * [количество выводимых результатов поиска](handlers/custom_handlers/find_hotel/region.py);
    * [минимальная цена проживания](handlers/custom_handlers/find_hotel/min_price.py) (для команды /bestdeal);
    * [максимальная цена проживания](handlers/custom_handlers/find_hotel/max_price.py) (для команды /bestdeal);
    * [нужно ли загружать фотографии отелей](handlers/custom_handlers/find_hotel/load_photos.py);
    * [количество загружаемых фотографий](handlers/custom_handlers/find_hotel/photo_amount.py) (если выбрана загрузка фотографий);
    * [дата прибытия](handlers/custom_handlers/find_hotel/arrival_date.py);
    * [дата убытия](handlers/custom_handlers/find_hotel/departures_date.py).
3. подтверждение введенных данных;
4. вывод результатов [с фотографиями](handlers/custom_handlers/find_hotel/send_with_photo.py) или [без](handlers/custom_handlers/find_hotel/send_hotels.py).
<!---->
Изменение контекста в каждой из команды происходит с использованием BDP(Behavioral Design Pattern - Поведенческий паттерн) Finite-state machine.  
Описание состояний бота приведено в [<code>__states package__</code> ](states) 
Так же реализован механизм __корректировки введенных данных__. Для этого пользователь на моменте подтверждения может выбрать любой из пунктов опроса и изменить его, а после подтвердить измененные данные, либо изменить другое поле.  
При выводе результата с фотографиями возможно переключение между фото с использованием __пагинатора__.

