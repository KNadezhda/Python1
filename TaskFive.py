proceeds = int(input("Введите выручку фирмы :"))
expenses = int(input("Введите издержки фирмы :"))
if proceeds > expenses:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {proceeds / expenses:.2f}")
    co_worker = int(input("Введите количество сотрудников фирмы :"))
    print(f"прибыль в расчете на одного сторудника сотавила {proceeds / co_worker:.2f}")
elif proceeds == expenses:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
