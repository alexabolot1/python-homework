"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
 ситуацию и не завершиться с ошибкой.
"""


class ZeroDiv(ZeroDivisionError):
    def __init__(self, cls_dividend, cls_divider):
        self.dividend = cls_dividend
        self.divider = cls_divider
        print(f'Деление {self.dividend} на {self.divider} невозможно, поскольку на {self.divider} делить нельзя!')


dividend = int(input('Введите делимое: '))
divider = int(input('Введите делитель: '))
try:
    print(f'Результат деления: {dividend / divider}')
except ZeroDivisionError:
    ZeroDiv(dividend, divider)
