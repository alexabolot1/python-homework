"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
 год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
 месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def converting(cls, date):
        date_int_list = [int(i) for i in date.split('-')]
        return date_int_list

    @staticmethod
    def validation(date):
        if Date.converting(date)[0] < 1 or Date.converting(date)[0] > 31:
            return print('Вы ввели некорректную дату!')
        elif Date.converting(date)[1] < 1 or Date.converting(date)[1] > 12:
            return print('Вы ввели некорректную дату!')
        elif Date.converting(date)[2] < 1904 or Date.converting(date)[1] > 2021:
            return print('Вы ввели некорректную дату!')
        else:
            return print('Все в порядке, вы ввели корректную дату!')


print(Date.converting('12-05-1998'))
Date.validation('12-12-1998')
