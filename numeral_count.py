# Счетчик цифр
# Задача ПРиоритет ЗадаЧ


def numeral_count(total_tasks):
    biggest_num = 0
    for num in range(total_tasks):
        number = int(input('Введите число: '))
        if number < 0:
            number = 0
        if number > biggest_num:
            biggest_num = number
    return biggest_num


total_tasks = int(input('Введите количество задач: '))
print('Первая задача на обработку:', numeral_count(total_tasks))
