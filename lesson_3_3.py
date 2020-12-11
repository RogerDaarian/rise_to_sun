# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


mapper = {
    'one': int(input("Первый аргумент")),
    'two': int(input("Второй аргумент")),
    'Three': int(input("Третий аргумент"))
}

small_val = mapper.items()
small_val_list = list(small_val)
print(small_val_list)

sv = min(small_val_list)
print(sv)
sv = min(small_val_list, key=lambda i : i[1])
print(sv)
small = sv[1]
print(small)
small_val_list.pop(small)
biggest_one = small_val_list[0]
bgo = biggest_one[1]
biggest_two = small_val_list[1]
bgt = biggest_two[1]
print(bgo, bgt)