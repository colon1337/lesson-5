def f(a):
    if a == 1:
        return 0
    elif a in (2, 3):
        return 1
    elif a >= 4:
        return f(a - 1) + f(a - 2)


a=input('Введите, какое число Фибоначчи надо найти:')
try:
    a=int(a)
    print(f'Нужное число: {f(a)}')
except ValueError:
    try:
        a=float(a)
        print('Вы ввели не целое число!')
    except ValueError:
        print('Вы ввели не число!')




