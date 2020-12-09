# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


# Вариант 1
z = [5, 'sector', 3.5, None]
x= type(z[0])
print(x)
x = type(z[1])
print(x)
x = type(z[2])
print(x)
x = type(z[3])
print(x)

# Вариант 2

full_list = [5, 15, 199.9, False, 'desepticon']
findings = f"Выбраны значения: {full_list}"
print(findings)
full_list.reverse()
amount = len(full_list)
print("Всего значений: ", amount)
count = 0
target = 0
stop = 0
while count != amount:
    target = (amount - 1) - count
    if type(full_list[target]) == int:
        print(count, "значение имеет тип int")
        count = count + 1
    elif type(full_list[target]) == float:
        print(count, "значение имеет тип float")
        count = count + 1
    elif type(full_list[target]) == str:
        print(count, "значение имеет тип str")
        count = count + 1
    elif type(full_list[target]) == bool:
        print(count, "значение имеет тип bool")
        count = count + 1
    elif type(full_list[target]) == list:
        print(count, "значение имеет тип list")
        count = count + 1
    elif type(full_list[target]) == tuple:
        print(count, "значение имеет тип tuple")
        count = count + 1
    elif type(full_list[target]) == dict:
        print(count, "значение имеет тип dict")
        count = count + 1
else:
    print("Всё сделано, капитан!")



