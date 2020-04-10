def my_func(x, y):
    return 1 / x ** abs(y)


print(my_func(2, -5))

''''''
"""вариант 2"""


def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(my_func(float(input("Введите положительное число ​x: ")), int(input("Введите целое отрицательное число y: "))))
