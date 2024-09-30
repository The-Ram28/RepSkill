# функция, вычисляющую Наибольший Общий Делитель двух чисел

def gcd(number_one, number_two):
    for num in range(number_one, 0, -1):
        big = number_two % num
        little = number_one % num
        if big == 0 and little == 0:
            return num


number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))
print(f'Наибольший общий делитель = {gcd(number_one, number_two)}')
