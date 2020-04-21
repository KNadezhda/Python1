"""
1)Реализуйте базовый класс Car
атрибуты: speed, color, name, is_police (булево)
методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
метод show_speed, который должен показывать текущую скорость автомобиля.
2)Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
3)Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км\ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость TownCar {self.name} - {self.speed} км\ч')

        if self.speed > 40:
            return f'{self.name} - для TownCar скорость выше допустимой'
        else:
            return f'{self.name} - скорость в пределах допустимой'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость WorkCar {self.name} - {self.speed} км\ч')

        if self.speed > 60:
            return f'{self.name} - для WorkCar скорость выше допустимой'
        else:
            return f'{self.name} - скорость в пределах допустимой'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


s = SportCar(100, 'blue', 'Porsсhe', False)
t = TownCar(50, 'White', 'Mitsubishi', False)
w = WorkCar(60, 'Rose', 'Gazelle', False)
p = PoliceCar(110, 'Blue',  'Ford', True)
print(w.turn_left())
print(f'{t.turn_right()}, {s.stop()}')
print(f'{w.go()}, {t.stop()}')
print(f'{t.name}, {t.color}')
print(f'Полицейский автомобиль {s.name}, {s.is_police}')
print(f'Полицейский автомобиль {t.name}, {t.is_police}')
print(f'Полицейский автомобиль {p.name}, {p.is_police}')
print(s.show_speed())
print(p.show_speed())
print(w.show_speed())