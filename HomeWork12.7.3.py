
money = float(input("Введите сумму "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = per_cent.values()
procents = []
for i in deposit:
    i = i * money / 100
    procents.append(i)


print("Максимальная сумма, которую вы можете заработать: " + str(int(max(procents))))