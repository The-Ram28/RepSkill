# 1 функция находит сумму всех цифр, 2-я считает количество цифр. В ответе разность суммы и количества
def summ(number):
    total_summ = 0
    while number > 0:
        total_summ += number % 10
        number //= 10
    print('Сумма чисел', total_summ)
    return total_summ


def numeral_count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    print('Количество чисел:', count)
    return count

number = int(input('Введите число: '))
summ = summ(number)
numeral_count = numeral_count(number)
print('Разность суммы и количества цифр:', abs(summ - numeral_count))
