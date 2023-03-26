Тестируемый сайт https://b2c.passport.rt.ru 

 Разработаны тест-кейсы и потенциальные баги:  https://docs.google.com/spreadsheets/d/1HPMvhu7v-Slo-Fo3Jc3UwT8NlgoQm4E9VKTyozKF-Mw/edit?usp=sharing
 При разработке тест-кейсов были применены следующие техники тест-дизайна: эквивалентное разбиение, анализ граничных значений, таблица принятия решений, диаграмма перехода состояния , попарное тестирование (Pairwise)

По всем кейсам созданы автотесты см.test_rostelekom.py
Для запуска тестов используйте python -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_rostelekom.py

В проверках используется браузер GooglHrome, соответствующий драйвер лежит в папке /tests, при необходимости можно его заменить на драйвер другого браузера, тогда необходимо будет произвести правки в файле tests/conftest.py 

config.py - в файле хранятся тестовые данные
requirements.txt - необходимые библиотеки
Base_page.py - классы с основными действиями на главной странице 
Main_page.py - класс с локаторами

