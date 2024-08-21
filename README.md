

**Weather Bot**

Простой бот погоды, который получает текущую погоду по вашему IP-адресу.

**Функции**

* Получает текущую погоду с помощью API OpenWeatherMap
* Отображает температуру, описание погоды, направление ветра и скорость ветра
* Отображает время восхода и заката солнца
* Поддерживает команду помощи для отображения возможностей бота

**Установка**

1. Клонируйте репозиторий: `git clone https://github.com/your-username/weather-bot.git`
2. Установите зависимости: `pip install -r requirements.txt`
3. Настройте свой ключ API OpenWeatherMap: `cp config.py.example config.py` и введите свой ключ API
4. Запустите бота: `python bot.py`

**Использование**

1. Начните разговор с ботом
2. Отправьте команду `/help` для отображения возможностей бота
3. Отправьте команду `/weather` для получения текущей погоды
4. Отправьте команду `/wind` для получения направления и скорости ветра
5. Отправьте команду `/sun_time` для получения времени восхода и заката солнца

**Ключи API**

* Ключ API OpenWeatherMap: получите на [https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)

**Зависимости**

* `aiogram` для API Telegram-бота
* `aiohttp` для отправки запросов API
* `dataclasses` для моделирования данных
* `enum` для перечислений

**Лицензия**

Лицензия MIT

**Вклад**

Вклады приветствуются! Отправьте pull-запросы или сообщения об ошибках.

**Благодарности**

* API OpenWeatherMap за предоставление данных о погоде
* Библиотека aiogram за предоставление функциональности API Telegram-бота