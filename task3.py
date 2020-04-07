month = int(input("Введите месяц в виде целого числа: "))
seasons_dict = {
    1: 'зима',
    2: 'весна',
    3: 'лето',
    4: 'осень'
}
if month == 12 or month == 1 or month == 2:
    print(seasons_dict[1])

elif month == 3 or month == 4 or month == 5:
    print(seasons_dict[2])

elif month == 6 or month == 7 or month == 8:
    print(seasons_dict[3])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict[4])

else:
    print("Месяц введен неверно. Введите месяц в виде целого числа: ")

''''''
seasons_list = ['зима', 'весна', 'лето', 'осень']
month = int(input("Введите месяц в виде целого числа: "))

if month == 12 or month == 1 or month == 2:
    print(seasons_list[0])

elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])

elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])

else:
    print("Месяц введен неверно. Введите месяц в виде целого числа: ")
