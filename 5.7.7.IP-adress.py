# Задание 7. IP-адрес 2
# Напишите программу, которая определяет, действительно ли заданная строка — правильный IP-адрес.
# Обеспечьте контроль ввода, где предусматривается добавление целых чисел от 0 до 255 и точек между ними.


good_ip = True
while True:
    good_ip = True
    user_ip = input('Введите IP: ').split('.')
    if len(user_ip) < 4 or len(user_ip) > 4:
        print('Адрес - это четыре числа, разделенные точками.')
    else:
        for i in user_ip:
            if not i.isdigit():
                print('{} - это не целое число.'.format(i))
                good_ip = False
            elif int(i) > 255:
                print('{} превышает 255.'.format(i))
                good_ip = False
        if good_ip:
            print('IP-адрес корректен.')
            break