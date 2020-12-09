# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# preform = input("Введите несколько слов, разделяя их пробелом: ")
# data = preform.split(' ')
# print("Вы ввели: ", data)
#
# for i, item in enumerate(data):
#     print(i + 1, item)

# Не смог сделать так, чтобы слова переносились, если в них больше 10 символов!!! Помогите

preform = input("Введите несколько слов, разделяя их пробелом: ")
data = preform.split(' ')
print("Вы ввели: ", data)
words = len(data)
print("Количество введённых слов: ", words)
cnt_letters = 0
cnt = 0

while cnt < words:
    def findLen(str):
        counter = 0
        for i in str:
            counter += 1
        return counter
    str = data[cnt]
    print(findLen(str))
    cnt = cnt + 1

    # if findLen(str) < 10:
    #         print(data[cnt])
    # elif findLen == 10:
    #         data[cnt] = data[cnt[:10]]


    # counter_1 = counter
    # if counter < 10:
    #     print(data[cnt])
    # elif cnt == 10:
    #     data[cnt] = data[cnt[:10]]

for i, item in enumerate(data):
    print(i + 1, item)