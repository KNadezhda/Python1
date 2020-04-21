"""
класс Road (дорога)
атрибуты (сделать защищенными): length (длина), width(ширина)
метод расчета массы асфальта
Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна
20м*5000м*(25кг*5см - объем) = 12500 т
Проверить работу метода.
данных атрибутов должны передаваться при создании экземпляра класса

"""
i = 0
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class AsphaltMass(Road):
    def __init__(self, _length, _width, volume, thickness):
        super().__init__(_length, _width)
        self.volume = volume
        self.thickness = thickness

    def massCount(self):
        return self.volume * self.thickness


r = AsphaltMass(20, 5000, 25, 5)
print((r.mass() * r.massCount()) / 1000)