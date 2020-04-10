word = input("Ввести слова через пробел: ")


def my_func(some):
    name = word.split()
    new_name =[i.capitalize() for i in name]
    return new_name


print(my_func(word))