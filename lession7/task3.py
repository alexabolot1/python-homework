"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
 В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
 В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
  вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
  только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
  соответственно. В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
 двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
 Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
"""


class Cell:
    def __init__(self, numb):
        self.numb = numb

    def __str__(self):
        return str(self.numb)

    def __add__(self, other):
        return Cell(self.numb + other.numb)

    def __sub__(self, other):
        if self.numb > other.numb:
            return Cell(self.numb - other.numb)
        else:
            return 'Вычитание невозможно'

    def __mul__(self, other):
        return Cell(self.numb * other.numb)

    def __truediv__(self, other):
        if other.numb != 0:
            return Cell(round(self.numb / other.numb, 2))
        else:
            return 'Деление клеток невозможно'

    def make_order(self, quantity):
        return '\n'.join(['*' * quantity for _ in (range(self.numb // quantity))]) + '\n' + '*' * (self.numb % quantity)


cell_1 = Cell(50)
cell_2 = Cell(12)
cell_3 = Cell(13)
print(f'Результат сложения клеток: {cell_1 + cell_2 + cell_3}')