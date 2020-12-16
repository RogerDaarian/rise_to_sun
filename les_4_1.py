# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv
# hour = int(input("Выработка в часах: "))
# cash = int(input("Ставка в час: "))
# prem = int(input("Премия для сотрудника: "))

def salary(hour, cash, prem):
    return prem + (hour * cash)

file_path, hour, cash, prem = argv
try:
    hour = int(hour)
    cash = int(cash)
    prem = int(prem)
except ValueError as err:
    print(f"Error: {err}")
# print(salary(hour, cash, prem))
print(salary(int(hour), int(cash), int(prem)))
print(argv)