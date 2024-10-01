# Монетка 2
# Поиск монет с заданными координатами
import math

def pyth(a, b, radius):
    c = math.sqrt(a ** 2 + b ** 2)
    if c > radius:
        return 'Монетки в области нет'
    else:
        return 'Монетка где-то рядом'

print('Введите координаты монетки:')
x = float(input('x: '))
y = float(input('y: '))
radius = float(input('Введите радиус: '))
print(pyth(x, y, radius))