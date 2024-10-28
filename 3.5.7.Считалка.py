# Задание 7. Считалка
# Напишите программу, которая выводит число от 1 до N — это номер человека, который останется в кругу последним.

humans_num = int(input('Количество человек: '))
number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number}-й человек')
humans = list(range(1, humans_num + 1))
index = 0
for _ in range(humans_num - 1):
    print('\nТекущий круг людей:', humans)
    start_count = index % len(humans)
    index = (start_count + number - 1) % len(humans)
    print('Начало счета с номера', humans[start_count])
    print('Выбывает человек под номером', humans[index])
    humans.remove(humans[index])
    print()

print('Остался человек по номером', humans[0])