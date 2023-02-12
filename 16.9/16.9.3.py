class Customer:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance


customers = [ # список клиентов
    {"first_name": "Иван",
     "last_name": "Петров",
     "city": "Москва",
     "balance": "50"
},
     {"first_name": "Мария",
     "last_name": "Иванова",
     "city": "Спб",
     "balance": "100"
}
]

for customer in customers:
    obj = Customer(first_name = customer.get("first_name"), #достаем данные по каждой категории для каждого клиента
                  last_name = customer.get("last_name"),
                  city = customer.get("city"),
                   balance = customer.get("balance"))

    print(obj.first_name, obj.last_name, ".",obj.city, ".", "Баланс:", obj.balance, "руб.") # выводим результат в формате указанном в задании