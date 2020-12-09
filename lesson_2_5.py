# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

data = [9, 7, 5, 5, 4, 1]
data_inp = int(input("Введите оценку от 1 до 9: "))
search_value = 0
search_value_sm = 0

if data_inp in data:
    search_value = data.index(data_inp)
    print(search_value)
    search_value_sm = data.index(data_inp - 1)
    if search_value_sm != data.index(data_inp - 1):
        search_value_sm = data.index(data_inp - 2)
        if search_value_sm != data.index(data_inp - 2):
           search_value_sm = data.index(data_inp - 3)
           if search_value_sm != data.index(data_inp - 3):
              search_value_sm = data.index(data_inp - 4)
              if search_value_sm != data.index(data_inp - 4):
                 search_value_sm = data.index(data_inp - 5)
                 if search_value_sm != data.index(data_inp - 5):
                    search_value_sm = data.index(data_inp - 6)
                    if search_value_sm != data.index(data_inp - 6):
                       search_value_sm = data.index(data_inp - 7)
                       if search_value_sm != data.index(data_inp - 7):
                          search_value_sm = data.index(data_inp - 8)
    print(search_value_sm)
else:
    print("Такого значения нет")




# while

# data.insert(x, data_inp)
# print(data)
#
# print(data.index(data_inp, data_inp))