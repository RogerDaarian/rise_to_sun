print("Summ")

number = int(input("Введите число от 1 до 9"))
second = number * 11
third = number * 111
conglutination = f"Summ: {number} + {second} + {third}"
result = int(number) + int(second) + int(third)
print("Result: %s = %d" % (conglutination, result))