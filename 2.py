# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Material:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_coat(self):
        return self.width / 6.5 + 0.5

    def get_suit(self):
        return self.height * 2 + 0.3

    @property
    def all_square(self):
        return str(f'Общая площадь ткани равна: '
                   f'{round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')


class Coat(Material):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто равна: {self.coat}'


class Suit(Material):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани костюма равна: {self.suit}'


coat = Coat(1, 3)
suit = Suit(2, 4)

print(coat)
print(suit)
print(coat.all_square)
print(suit.all_square)
