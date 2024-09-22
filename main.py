def summ(number):
    total_summ = 0
    while number > 0:
        total_summ += number % 10
        number //= 10
    print('Сумма цифр равны', total_summ)
    main()


def maximum(number):
    max_num = 0
    while number > 0:
        n = number % 10
        if max_num < n:
            max_num = n
        number //= 10
    print('Максимальная цифра =', max_num)
    main()


def minimum(number):
    min_num = 9
    while number > 0:
        n = number % 10
        if min_num > n:
            min_num = n
        number //= 10
    print('Минимальная цифра =', min_num)
    main()


def main():
    action = int(input(
        'Выберите действие. 1-> сумма цифр, 2-> максимальная цифра, 3-> минимальная цифра '))
    if action == 1:
        summ(number)
    elif action == 2:
        maximum(number)
    elif action == 3:
        minimum(number)
    else:
        print('Ошибка! Выберите действие!')
        main()


number = int(input('Введите число: '))

main()
