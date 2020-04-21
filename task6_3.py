"""
1)базовый (родительский) класс Worker (работник)
2)атрибуты: name, surname, position (должность), income (доход)
3)income (доход)- атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}
4)Создать класс Position (должность) на базе класса Worker
5)В классе Position реализовать методы
получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income)
6)Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, qualification, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.qualification = qualification

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def factor(self):
        return self.qualification

    def get_total_income(self):
        #return self._income.get('wage') + self._income.get('bonus')
        return f'{sum(self._income.values())}'

a = Position('Ivan', 'Petrov', 'engineer', 3, 100000.0, 25000.0)
print(a.get_full_name())
print(a.position)
print(a.factor())
print(a.get_total_income())