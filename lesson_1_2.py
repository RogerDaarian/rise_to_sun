print("Second")

some_data = int(input("Введите число в секундах: "))
h = some_data // 3600
m = (some_data // 60) % 60
s = some_data % 60
print("Time info: %02d:%02d:%02d" % (h, m, s))