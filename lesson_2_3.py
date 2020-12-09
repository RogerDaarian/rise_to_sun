# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Внимание!!! В этом файле 2 варианта достижения желаемого!

#  Вариан 1. С if-аками. Для тех, кто любит заморочиться:).
#
# def one():
#     print("Январь")
#
# def two():
#     print("Февраль")
#
# def three():
#     print("Март")
#
# def four():
#     print("Апрель")
#
# def five():
#     print("Май")
#
# def six():
#     print("Июнь")
#
# def seven():
#     print("Июль")
#
# def eight():
#     print("Август")
#
# def nine():
#     print("Сентябрь")
#
# def ten():
#     print("Октябрь")
#
# def eleven():
#     print("Ноябрь")
#
# def twelve():
#     print("Декабрь")
#
#
# in_month = input("Введите номер месяца, указав от 1 до 12: ")
#
# one == 1
# two == 2
# three == 3
# four == 4
# five == 5
# six == 6
# seven == 7
# eight == 8
# nine == 9
# ten == 10
# eleven == 11
# twelve == 12
#
# if in_month == '1':
#     one()
# elif in_month == '2':
#     two()
# elif in_month == '3':
#     three()
# elif in_month == '4':
#     four()
# elif in_month == '5':
#     five()
# elif in_month == '6':
#     six()
# elif in_month == '7':
#     seven()
# elif in_month == '8':
#     eight()
# elif in_month == '9':
#     nine()
# elif in_month == '10':
#     ten()
# elif in_month == '11':
#     eleven()
# elif in_month == '12':
#     twelve()
# else:
#     raise ValueError("Вы указали номер месяца не верно")
#
#
#
#
#
#
#
#
#
#  Вариант 2. - Всего что я смог добиться, как бы не старался, это распознание месяца по
# словам: one, two и т.д. Подскажите, пожалуйста, где не прав? В dev one() - туда просто не запишешь
# после dev единицу, он ругается:SyntaxError: invalid syntax
#

#
# def one():
#     print("Январь")
#
# def two():
#     print("Февраль")
#
# def three():
#     print("Март")
#
# def four():
#     print("Апрель")
#
# def five():
#     print("Май")
#
# def six():
#     print("Июнь")
#
# def seven():
#     print("Июль")
#
# def eight():
#     print("Август")
#
# def nine():
#     print("Сентябрь")
#
# def ten():
#     print("Октябрь")
#
# def eleven():
#     print("Ноябрь")
#
# def twelve():
#     print("Декабрь")
#
#
# mapper = {
#     'one': one,
#     'two': two,
#     'three': three,
#     'four': four,
#     'five': five,
#     'six': six,
#     'seven': seven,
#     'eight': eight,
#     'nine': nine,
#     'ten': ten,
#     'eleven': eleven,
#     'twelve': twelve
# }
#
# in_month = input('Введите номер месяца, указав от 1 до 12: ')
#
# mapper[in_month]()