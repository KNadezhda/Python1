def s_div():
    try:
        a_val = float(input('Введите число a: '))
        b_val = float(input('Введите число b: '))
    except ValueError:
        return
    if b_val == 0:
        return float(input('Введите положительное число b: '))
    div_val = a_val / b_val
    return div_val


c_val = s_div()
print(c_val)
