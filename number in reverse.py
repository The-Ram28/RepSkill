def coup(number):
    inverted_number = 0
    while number > 0:
        inverted_number *= 10
        inverted_number += number % 10
        number //= 10
    print('Число наоборот:', inverted_number)


def main():
    number = int(input('Введите число:'))
    if number > 0:
        coup(number)
        main()
    else:
        print('Программа завершена!')


main()
