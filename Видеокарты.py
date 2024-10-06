# Видеокарты
# программа, которая удаляет наибольшие элементы из списка видеокарт

old_list = []
number = int(input('Количество видеокарт: '))
for i in range(number):
    print(f'Видеокарта {i + 1}:', end='')
    card = int(input())
    old_list.append(card)

new_list = []
for index in old_list:
    if index < max(old_list):
        new_list.append(index)

print('Старый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)