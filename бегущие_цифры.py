# Бегущие цифры
# Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций.

num_list = [1, 4, -3, 0, 10]
shift = int(input('Сдвиг: '))
print('Изначальный список:', num_list)
for _ in range(shift):
    cash = num_list[-1]
    for num in range(-1, -len(num_list), - 1):
        num_list[num] = num_list[num - 1]
    num_list[0] = cash
print('Сдвинутый список:', num_list)