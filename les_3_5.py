# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале
# нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

preform = ['начало']
data = preform
print(data)
end = '*'
result = 0

while end not in data:
    if end not in data:
        preform = input("Введите числа, разделяя их пробелом")
        data = preform.split(' ')
        print(data)
        count_len = len(data)
        num_len = count_len - 1
        summ = 0
        while count_len != 0 and end not in data:
            try:
                end in data == True
            except ValueError: break
            summ = int(data[num_len]) + summ
            num_len = num_len - 1
            count_len = count_len - 1
        else:
            print("Сумма чисел на данный момент равна: ", summ)
            result = result + summ
            print("Сумма всех введённых чисел равна: ", result)