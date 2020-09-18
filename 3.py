# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __str__(self):
        return f'результат операции: {self.qty * "*"}'

    def __add__(self, other):
        add = self.qty + other.qty
        return Cell(add)

    def __sub__(self, other):
        sub = self.qty - other.qty
        if sub > 0:
            return Cell(sub)
        else:
            return f'Отрицательное число'

    def __mul__(self, other):
        mul = int(self.qty * other.qty)
        return Cell(mul)

    def __truediv__(self, other):
        truediv = round(self.qty // other.qty)
        return Cell(truediv)

    def make_order(self, cells):
        row = ''
        for i in range(int(self.qty / cells)):
            row += f'{"*" * cells} \\n'
        row += f'{"*" * (self.qty % cells)}'
        return row


cells1 = Cell(12)
cells2 = Cell(5)

print(f'Сложение, {cells1 + cells2}')
print(f'Вычетание, {cells2 - cells1}')
print(f'Умножение, {cells1 * cells2}')
print(f'Деление, {cells1 / cells2}')

print(cells2.make_order(5))
print(cells1.make_order(15))



