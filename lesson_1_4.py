print("biggest")

number = int(input("Пожалуйста, введите любое число"))
one = []
while number > 10:
    one.append(number % 10)
    number //= 10
done = max(one)
print(done)
