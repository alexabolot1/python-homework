"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
 Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
  начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from math import factorial
from random import randint


def generator(arg):
    for fact in arg:
        yield factorial(fact)


my_list = [randint(5, 15) for i in range(1, 10)]
print(my_list)

for i in generator(my_list):
    print(i)
