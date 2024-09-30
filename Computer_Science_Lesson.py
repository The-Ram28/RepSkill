# Урок информатики 2

from decimal import Decimal


def formula(x):
    if x <= 0:
        return "Число должно быть больше нуля."

    b = 0
    a = x
    while a > 10:
        a /= 10
        b += 1
    while a < 1:
        a *= 10
        b -= 1

    return f'x = {a} * 10 ** {b}'


x = float(input("Введите число: "))
print(formula(x))
