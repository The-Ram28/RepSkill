# Задача 2. Универсальная программа
# Напишите функцию, возвращающую список элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс — это простое число.
# Для проверки на простое число напишите отдельную функцию is_prime.

def is_prime(number):
    if number > 1:
        for i_num in range(2, number):
            if number % i_num == 0:
                return False
        return True

def crypto(object):
    return [value for index, value in enumerate(object) if is_prime(index)]

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))