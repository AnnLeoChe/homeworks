valid_email = "anehka-88@mail.ru"
valid_pass = "QwertyQwerty123"

invalid_email = 'anehka-88888@mail.ru'
invalid_pass = 'QWERTYYUII35456'

name = 'Анна'
surname = 'Чемоданова'
region = 'Москва г'
email = 'anehka-8888@mail.ru'
password = 'Zxc12345'

false_email = '123456'
false_mobile_max = '891178945236'
false_mobile_mini = '8911789452'
false_name_mini = 'А'
name_two_letters = "Он"
thirty_letters = 'йцукенгшщзхъфывапролджэячччч'
thirty_one_letters = 'йцукенгшщзхъфывапролджэячсмитьбюЁ'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
