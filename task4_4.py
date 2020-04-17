from random import randint

my_list = [randint(-10, 10) for i in range(50)]

print(f"сгенерированный список\n{my_list}")

my_new_list = [el for el in my_list if my_list.count(el) == 1]

print(f"список по  условию\n{my_new_list}")