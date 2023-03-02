from api import PetFriends
from settings import *
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0



def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age= '4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


""" Задание 19.7.2 """

#1

def test_get_api_key_without_valid_user(email=invalid_email, password=invalid_password):
    """ Проверяем что  незарегестрированный пользователь не сможет зайти на сайт (код 403(из swagger)) и получить ключ"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert not 'key' in result

#2

def test_get_api_key_without_valid_password(email=valid_email, password=invalid_password):
    """ Проверяем что  зарегестрированный пользователь  с неправильным паролем не сможет зайти на сайт (код 403 (из swagger)) и получить ключ"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert not 'key' in result

#3

def test_add_new_pet_without_valid_data(name='', animal_type='',
                                     age=''):
    """Проверяем что нельзя добавить питомца с пустыми  данными, код ответа 400 (из swagger)"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 400

#4

def test_get_all_pets_without_valid_key(filter=''):
    """ Проверяем что запрос списка питомцев c неправильным ключем вернет нам статус  403 (из swagger)"""

    status, result = pf.get_list_of_pets(invalid_key, filter)

    assert status == 403

#5
def test_failed_delete_another_pet():
    """Проверяем невозможность удаления чужого питомца под своим ключем
    (!) Тест заканчивается со статусом FAIL т.к. он отлавливает баг"""

    # Получаем ключ auth_key первого пользователя
    _, auth_key1 = pf.get_api_key(valid_email, valid_password)

    # Получаем ключ запрашиваем список  питомцев второго пользователя
    _, auth_key2 = pf.get_api_key(valid_email2, valid_password2)
    _, second_user_pets = pf.get_list_of_pets(auth_key2, "my_pets")

    # Проверяем - если список второго пользователя  питомцев пустой, то добавляем нового
    if len(second_user_pets['pets']) == 0:
        pf.add_new_pet(auth_key2, "котюня", "кот", "10", "images/cat1.jpg")
        _, second_user_pets = pf.get_list_of_pets(auth_key2, "my_pets")

    # Берём id первого питомца из списка второго пользователя и отправляем запрос на удаление под ключем первого пользователя
    pet_id = second_user_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key1, pet_id)

    # Ещё раз запрашиваем список  питомцев второго пользоватенля
    _, second_user_pets = pf.get_list_of_pets(auth_key2, "my_pets")

    # Проверяем что статус ответа равен 403 (из swagger) и в списке питомцев второго пользователя  не исчезло  id питомца что пытались удалить
    assert status == 403
    assert pet_id in second_user_pets.values()

#6
def test_update_another_pet_info(name='pesik_new', animal_type='dog', age='10'):
    """Проверяем возможность обновления информации о чужом питомце
    (!) Тест заканчивается со статусом FAIL т.к. он отлавливает баг"""

    # Получаем ключ auth_key первого пользователя
    _, auth_key1 = pf.get_api_key(valid_email, valid_password)

    # Получаем ключ запрашиваем список  питомцев второго пользователя
    _, auth_key2 = pf.get_api_key(valid_email2, valid_password2)
    _, second_user_pets = pf.get_list_of_pets(auth_key2, "my_pets")

    # Проверяем - если список второго пользователя  питомцев пустой, то добавляем нового
    if len(second_user_pets['pets']) == 0:
        pf.add_new_pet(auth_key2, "кот", "кот", "10", "images/cat1.jpg")

    # Берём id первого питомца из списка второго пользователя и отправляем запрос на изменение под ключом первого пользователя
    status, result = pf.update_pet_info(auth_key1, second_user_pets['pets'][0]['id'], name, animal_type, age)
    # Проверяем что статус ответа равен 403 (из swagger) и имя питомца не поменялось
    assert status == 403
    assert result['name'] != name

#7
def test_update_with_incorrect_data(name=' ', animal_type=' ', age=' '):
    """Проверяем возможность обновления информации о питомце некорректными(пустыми) данными
     (!) Тест заканчивается со статусом FAIL т.к. он отлавливает баг"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список  пустой, то добавляем питомца
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "пес", "бобик", "1", "images/dog.png")

    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа равен 400 (из swagger)  и имя питомца не поменялось
    assert status == 400
    assert result['name'] != name


#8
def test_add_new_pet_with_invalid_age(name='kisa', animal_type='pers',
                                     age='dva', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с некорректным возрастом, указанным не цифрами
     (!) Тест заканчивается со статусом FAIL т.к. он отлавливает баг"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Проверяем что статус ответа равен 400 (из swagger)
    assert status == 400

#9
def test_add_new_pet_with_invalid_photo_type(name='pes', animal_type='old',
                                     age='100', pet_photo='images/pes.gif'):
    """Проверяем что можно добавить питомца с некорректным расширением добавляемого фото
     (!) Тест заканчивается со статусом FAIL т.к. он отлавливает баг"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Проверяем что статус ответа равен 400 (из swagger)
    assert status == 400

#10
def test_positive_scenario(name='kisa', animal_type='pers', age='1', pet_photo='images/cat1.jpg'):
    """Проверяем сценарий: создаем нового питомца - одновляем данные по нему и удаляем питомца"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # создаем нового питомца
    status_add, new_pet = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    new_pet_id = new_pet['id'] # узнаем id созданного питомца
    print("создали питомца :", new_pet['name'], new_pet['animal_type'], new_pet['age'])

    # обновляем данные питомца
    status_update, update_pet = pf.update_pet_info(auth_key, new_pet_id, 'Bobby', 'dog', 0)
    print("обновили данные питомца на:", update_pet['name'], update_pet['animal_type'], update_pet['age'])

    # удаляем питомца
    status_delete, _ = pf.delete_pet(auth_key, new_pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статусы ответа равены 200 на всех операциях и проверяем что в списке питомцев нет id удалённого питомца
    assert status_add == 200
    assert status_update == 200
    assert status_delete == 200
    assert new_pet_id not in my_pets.values()