# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data
# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(response.status_code)

# Функция response.json() позволяет получить тело ответа в формате JSON.
# Это полезно для извлечения данных, полученных в результате запроса, 
# особенно когда сервер возвращает полезные данные в формате JSON.
# Здесь мы вызываем эту функцию и выводим полученный JSON в консоль для наглядности.
print(response.json())

# Импорт модуля requests для отправки HTTP-запросов
import requests
# Импорт конфигурационного файла, который содержит настройки URL
import configuration

# Функция для получения данных из таблицы пользователей
def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Выполнение функции и сохранение ответа в переменную response
response = get_users_table()

# Вывод статус-кода ответа сервера в консоль
# Статус-коды HTTP сообщают о результате выполнения запроса
print(response.status_code)
