# Задание 5. Пароль
# Напишите программу, которая просит пользователя придумать пароль до тех пор, пока этот пароль не станет
# надёжным. Должна использоваться латиница.

while True:
    password = input('Придумайте пароль: ')
    count_num = 0
    count_upp_sym = 0
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    for i_sym in password:
        if i_sym.startswith(numbers):
            count_num += 1
        if i_sym != i_sym.lower():
            count_upp_sym += 1
    if count_upp_sym >= 1 and count_num >= 3 and len(password) >= 8:
        print('Это надежный пароль.')
        break
    else:
        print('Пароль ненадежный. Попробуйте еще раз.')