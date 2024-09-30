# Число наоборот

# Функция переворота числа
def coup(number):
    inverted_number = 0
    while number > 0:
        inverted_number *= 10
        inverted_number += number % 10
        number //= 10
    return inverted_number


number_one = int(input('Введите первое число:'))
number_two = int(input('Введите второе число:'))
round_one = coup(number_one)
round_two = coup(number_two)
print('Первое число наоборот:', round_one)
print('Второе число наоборот:', round_two)
print('Сумма:', round_one + round_two)
print('Сумма наоборот: ', coup(round_one + round_two))
