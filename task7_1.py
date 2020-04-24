"""
класс Matrix (матрица),
метод __init__()), принимает (список списков) для формирования матрицы
Следующий шаг-перегрузка метода __str__() для вывода матрицы в привычном виде.
Следующий шаг-перегрузка метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result += str(self.matrix[i][j]) + "   "
            result += "\n"
        return result

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return self


m_1 = Matrix([[1, 2, 1], [3, 4, 2], [5, 6, 4]])
m_2 = Matrix([[7, 8, 5], [9, 10, 6], [11, 12, 9]])
print(m_1)
print(m_2)
print(m_1 + m_2)
