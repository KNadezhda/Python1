"""
1)Реализовать класс Stationery (канцелярская принадлежность).
2)Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
3)Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
4)В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
5)Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Ручка пишет чернилами, чернила невозможно удалить,\nпоэтому старайтесь писать без ошибок.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Карандаш со стержнем из графита,\nвы можете писать, рисовать, чертить,\nсделать наброски. Его можно стереть ластиком.'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Это цветной фломастер с широким стержнем для выделения строк,\nслов или отрезков текста, а также для плакатных работ.'


p = Pen('Ручка')
pl = Pencil('Карандаш')
h = Handle('Маркер')
print(p.draw())
print(pl.draw())
print(h.draw())