# Сумма чисел 2

def summa_n(n):
    summa = 0
    for num in range(1, n + 1):
        summa += num
    return summa


n = int(input('Введите число: '))

print(f'Сумма от 1 до {n} = {summa_n(n)}')
print(f'Сумма от 1 до {summa_n(n)} = {summa_n(summa_n(n))}')