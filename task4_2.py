my_list = [25, 4, 6, -9, 5, 20, 7, 11]
my_new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')