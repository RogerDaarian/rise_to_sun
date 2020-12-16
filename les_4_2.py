# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
len_lst = len(lst)
cnt = len_lst - (len_lst - 1)
cnt_s = cnt - 1
print(cnt, cnt_s)
data = 0

def incomming():
    cnt = len_lst - (len_lst - 1)
    cnt_s = cnt - 1
    data = 0
    if lst[cnt]>lst[cnt_s]:
        data = data + lst[cnt]
        cnt = cnt + 1
        return data, cnt
    yield data, cnt
    yield data, cnt

c = incomming()
print(data)
print(next(c))
print(next(c))