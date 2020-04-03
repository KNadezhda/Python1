time_s = int(input("Введите время в секундах:"))
hour = time_s // 3600
min = time_s % 3600 // 60
sec = time_s % 3600 % 60
print("%02d:%02d:%02d" % (hour, min, sec))
