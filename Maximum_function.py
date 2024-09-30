# Функция Максимума

def maximum_of_two():
    num_one = int(input('Введите первое число: '))
    num_two = int(input('Введите второе число: '))

    if num_one > num_two:
        return num_one
    else:
        return num_two


def maximum_of_three(num_one_two):
    num_three = int(input('Введите третье число: '))
    if num_one_two > num_three:
        return num_one_two
    else:
        return num_three


print('Наибольшее число:', maximum_of_three(maximum_of_two()))
