""" позиционные параметры"""
def my_func(var_1, var_2, var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    if var_1 >= var_2 and var_3 >= var_2:
        return var_1 + var_3
    else:
        return var_2 + var_3

print(my_func(5.578, 7, 5))