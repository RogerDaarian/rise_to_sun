proceeds = float(input("Введите значение выручки "))
expenses = float(input("Введите значение издержек "))
profit = proceeds - expenses
if proceeds > expenses:
    print("Поздравляем, доходность составила ", profit)
    people = float(input("Укажите количество сотрудников: "))
    people_profit = str(profit / people)
    print("Доходность на сотрудника равна " + people_profit)
elif proceeds < expenses:
    print("К сожалению, убытки составили ", profit)
elif proceeds == expenses:
    print("Вы сработали в ноль")