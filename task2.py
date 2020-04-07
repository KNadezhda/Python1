el_count = int(input("Введите количество элементов списка "))
# пустой список
my_list = []
# переменные
i = 0
el = 0
# создаем список пользователя
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
# задаем шаг и меняем индексы элементов местами
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2

print(my_list)