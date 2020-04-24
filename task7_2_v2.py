"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто/Coat) и рост (для костюма/Suit).
Это могут быть обычные числа: V/size/Coat и H/height/Suit, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""


class Overdress:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def get_param(self):
        return str(f'Площадь общая ткани \n'
                   f' {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')


class Coat(Overdress):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round((self.size / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Suit(Overdress):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_s = round((self.height * 2 + 0.3), 2)

    def __str__(self):
        return f'Площадь на костюм {self.square_s}'


mc = Overdress(56, 1.70)
print(mc.get_param)
ct = Coat(56, 1.70)
st = Suit(56, 1.70)
print(ct)
print(st)
