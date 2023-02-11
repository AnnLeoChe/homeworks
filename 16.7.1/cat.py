class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

import json
with open('cat_list.json', encoding='utf8') as f: #загружаем список кошек из файла
    cats = json.load(f) #присваваем полученный список словарей переменной cats
#print(cats) #служебная строка, проверяем что файл загрузился


for cat in cats:
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))

    print("Имя: ", cat_obj.name, " Пол: ", cat_obj.gender, " Возраст: ", cat_obj.age)
