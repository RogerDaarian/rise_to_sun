# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

preform = input("Введите данные, разделяя их пробелом: ")
data = preform.split(' ')
print("Вы ввели: ", data)
amount = len(data)
print("Всего значений: ", amount)
count_a = 0
count_b = 1
while amount > count_b:
    if data[count_a] == data[count_a]:
        a = data[count_a]
        b = data[count_b]
        a, b = b, a
        data[count_a] = a
        data[count_b] = b
        count_a = count_a + 2
        count_b = count_b + 2
    else:
        print("Чтото пошло не так")
print(data)

