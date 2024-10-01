# Функция, которая ищет наименьший делитель, отличный от 1.
def least_divisor(number):
    least_divisor = None
    for num in range(number, 1, -1):
        divisor = number % num
        if divisor == 0:
            least_divisor = num
    return least_divisor

number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', least_divisor(number))
