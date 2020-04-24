"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять:
увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
"""
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Клетка {self.quantity}'

    def __add__(self, other):
        # self.result = Cell(self.quantity + other.quantity)
        return Cell(str(self.quantity + other.quantity))

    def __sub__(self, other):

        if (self.quantity - other.quantity) > 0:
            return Cell(self.quantity - other.quantity)
        else:
            return f'Отрицательно!'

    def __mul__(self, other):
        self.result = Cell(int(self.quantity * other.quantity))
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        self.result = Cell(round(self.quantity / other.quantity))
        return Cell(round((self.quantity / other.quantity), 2))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(11)
cells2 = Cell(5)
cells3 = cells1 + cells2
print(cells1)
print(cells2)
print(f'результат сложения {cells3}')
print(f'результат вычитания {cells1 - cells2}')
print(f'результат умножения {cells1 * cells2}')
print(f'результат деления {cells1 / cells2}')
print(f'нарезка\n'f'{cells1.make_order(6)}')
print(f'нарезка\n'f'{cells2.make_order(3)}')