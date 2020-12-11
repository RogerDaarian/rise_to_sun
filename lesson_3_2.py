# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, date, sity, mail, phone):
    result = f"{name}{surname}{date}{sity}{mail}{phone}"
    return result

user_info = {
    'name': input("Введите ваше имя"),
    'surname': input("Введите вашу фамилию"),
    'date': input("Год рождения"),
    'sity': input("Город проживания"),
    'mail': input("email"),
    'phone': input("Телефон")
}

res = user_info
print(res)