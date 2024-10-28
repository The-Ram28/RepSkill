# Задание 8. Бегущая строка
# Напишите программу, которая определяет, можно ли получить первую строку из второй циклическим сдвигом.

first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')

shift = 1

if first_str == second_str:
    print('Строки одинаковые.')
else:
    if len(first_str) == len(second_str):
        while True:
            check = second_str[-shift:] + second_str[:-shift]
            if first_str == check:
                print('Первая строка получается из второй со сдвигом {}.'.format(shift))
                break
            elif shift == len(second_str):
                print('Первую строку нельзя получить из второй с помощью цикличного сдвига.')
                break
            else:
                shift += 1
    else:
        print('Строка имеет разную длину!')