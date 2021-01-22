""""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(a, b):
    if b != 0:
        if a / b % 2 != 0:
            return round(a / b, 2)
        else:
            return a // b
    else:
        return


def my_func_one():
    while True:
        number_one = int(input('Введите делимое '))
        number_two = int(input('Введите делитель '))
        if my_func(number_one, number_two) is None:
            print("На 0 делить нельзя! Давайте попробуем еще раз :)")
            continue
        else:
            break
    return print(f'Результат деления - {my_func(number_one, number_two)}')


my_func_one()
