"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
 — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
  У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
  числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
 для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, inp):
        self.inp = inp

    @abstractmethod
    def calc(self):
        pass


class Costume(Clothes):
    def calc(self):
        return print(f'Расход ткани на Ваш костюм с учтом размера составит: {round(2 * self.inp + 0.3, 2)}')


class Coat(Clothes):
    def calc(self):
        return print(f'Расход ткани на Ваш пальто с учётом размера составит: {round(self.inp / 6.5 + 0.5, 2)}')


coat = Coat(56)
costume = Costume(15)
coat.calc()
costume.calc()
