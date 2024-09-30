# функция, вычисляющую Наибольший Общий Делитель двух чисел

def least_divisor(big_num, litle_num):
    for num in range(litle_num, 0, -1):
        big = big_num % num
        little = litle_num % num
        if big == 0 and little == 0:
            print('наибольший общий делитель =', num)
            break


number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))

if number_one > number_two:
    least_divisor(number_one, number_two)
elif number_two > number_one:
    least_divisor(number_two, number_one)
