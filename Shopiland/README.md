АВТОМАТИЗАЦИЯ ТЕСТИРОВАНИЯ. ПРОЕКТ SHOPILAND.

Объект тестирования:
https://shopiland.ru/

Для тестирование использовались:
PyCharm IDE (+ необходимые библиотеки указаныне в requirements.txt) - для написание автотестов.
DevTools - для построения локаторов.

В папке pages содержатся исходные данные, локаторы, функции.
В папке tests содержатся тесты.

Для тестирования необходимо установить пакеты указанные в файле: requirements.txt 
Запуск автоматической установки pip3 install -r requirements.txt

Запуск тестов (путь к драйверу необходимо изменить на актуальный):
python -m pytest -v --driver Chrome --driver-path C:\Projects\SeleniumDriver\Chrome\chromedriver.exe tests/test_search_page.py
