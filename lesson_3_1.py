# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
# их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации
# деления на ноль.

def pos_int(a, b):
    if b != 0:
        result = a / b
        print(result)
        return result
    else:
        raise ZeroDivisionError("Деление на ноль не возможно")

come = list(input("Введите два числа"))
come[0], come[1] = int(come[0]), int(come[1])
pos_int(come[0], come[1])
