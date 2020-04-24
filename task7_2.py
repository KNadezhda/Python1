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

from abc import ABCMeta, abstractmethod


class Overdress(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def change_gear(self):
        pass

    """@property - Честно. не могу придумать, что записать в этой ситуации в property"""


class Coat(Overdress):
    def __init__(self, size):
        self.size = size

    def change_gear(self):
        return round((self.size / 6.5 + 0.5), 2)


class Suit(Overdress):

    def __init__(self, height):
        self.height = height

    def change_gear(self):
        return round((self.height * 2 + 0.3), 2)


ct = Coat(56)
st = Suit(1.70)
print(f'Расход ткани на пальто: ' + str(ct.change_gear()))
print(f'Расход ткани на костюм: ' + str(st.change_gear()))
print(f'Общий асход ткани: ' + str(st.change_gear() + ct.change_gear()))
