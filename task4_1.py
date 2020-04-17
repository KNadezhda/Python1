from sys import argv

def sal():
    try:
        time, salary, bonus = map(float, argv[1:])
        """5.5, 10.25, 15.01"""
        #time = ('Выработка в часах ')
        #salary = ('ставка в час ')
        #bonus = ('Премия')
        res = (time * salary) + bonus
        print(f"sal - {res}")
    except ValueError:
        return print('Not a number')
sal()