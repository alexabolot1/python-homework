""""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def my_func(name_arg, surname_arg, year_arg, city_arg, email_arg, phone_arg):
    return print(f'Данного пользователя зовут {name_arg} {surname_arg}. Пользователь {year_arg} года рождения. '
                 f'Проживает в городе {city_arg}. Контактные '
                 f'данные: емейл - {email_arg}, номер телефона - {phone_arg}')


name = input("Введите ваше имя ")
surname = input("Введите вашу фамилию ")
year = int(input("Введите год вашего рождения "))
city = input("Введите ваш город ")
email = input("Введите ваш email ")
phone = int(input("Введите ваш номер через восмьерку "))

my_func(name_arg=name, surname_arg=surname, year_arg=year, city_arg=city, email_arg=email, phone_arg=phone)
