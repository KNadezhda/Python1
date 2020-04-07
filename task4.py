my_str = input("Введите нескольких слов, разделённых пробелами: ")
word = my_str.split(' ')
for i, el in enumerate(word, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}) {el}")
