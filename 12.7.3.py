
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("money= ")) #вводим вклад и переводим его в численный формат
deposit =[] # создаем список куда будем записывать размер депозитов

for v in per_cent.values():
    deposit.append(v*money/100) #вычисляем накопленные средства и заносим их в список deposit

max_deposit=max(deposit) #вычисляем максимальное значение
print('deposit=', deposit)
print('Максимальная сумма, которую вы можете заработать —',max_deposit)
