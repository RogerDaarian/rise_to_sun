a = float(input("Количество километров сейчас"))
b = float(input("Желаемое количество километров"))
x = 1.1
cnt = a
day = 0
while cnt < b:
    cnt = cnt * x
    day = day + 1
    print("Новый результат составил " + str(cnt))
if b >= a:
    result = f"Вы достигли результата, пробежав не менее {b} киллометров за {day} дней"
    print(result)

