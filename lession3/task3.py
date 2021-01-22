"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    summa = my_list[0] + my_list[1]
    return summa


argument_one = int(input('Введите первое число: '))
argument_two = int(input('Введите второе число: '))
argument_three = int(input('Введите третье число: '))

print('Сумма наибольших двух введёных вами чисел равна:  ',
      my_func(argument_one, argument_two, argument_three))
