# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

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

for i, item in enumerate(data):
    print(i + 1, item[:10])