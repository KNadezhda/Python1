n = 0
try:
    while True:
        for i in map(int, input("Введите строку чисел, разделенных пробелом: ").split()):
            n += i
        print(n)
except ValueError:
    print(n)
