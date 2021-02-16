"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
 будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
  В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
  уникальные для каждого типа оргтехники.
"""

"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в 
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class OfficeEquipment:
    def __init__(self, name, color, inv_numb, price):
        self.name = name
        self.color = color
        self.inv_numb = inv_numb
        self.price = price
        self.storage = []

    def __str__(self):
        return f'Товар {self.name}.\nЦвет: {self.color}.\nИнвентарный номер: {self.inv_numb}.\nЦена: {self.price}'

    def reception(self):
        try:
            product_quantity = int(input(f'Введите кол-во единиц {self.name}, которое нужно добавить на склад: '))
            product_dict = {'Название товара': self.name,
                            'Цена товара': self.price,
                            'Количество единиц товара': product_quantity}
            self.storage.append(product_dict)
            print(f'Теперь на складе: {self.storage}')
            # никак не могу понять, что должен вернуть метод, чтобы self.storage не перезаписывался,
            # а добавлял новые словари
        except ValueError:
            return print('Ошибка ввода')


class Printer(OfficeEquipment):
    def printer(self):
        return f'{self.name} печатает.'


class Scanner(OfficeEquipment):
    def scanner(self):
        return f'{self.name} сканирует.'


class Phone(OfficeEquipment):
    def phone(self):
        return f'{self.name} принимает звонки.'


printer = Printer('Принтер "HP"', 'чёрный', 54524, 1500)
phone = Phone('Телефон стационраный', 'белый', 374575, 1000)
scanner = Scanner('Сканер "CANON"', 'серый', 1057575, 2000)
printer.reception()