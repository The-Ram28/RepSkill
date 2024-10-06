# Контейнеры
# Программа выводит номер, под которым будет лежать новый контейнер.

stockroom = []
number = int(input('Количество контейнеров: '))
for _ in range(number):
    container = int(input('Введите вес контейнера: '))
    if container > 200:
        print('Ошибка, вес контейнера не должен превышать 200!')
        continue
    stockroom.append(container)

new_container = int(input('Введите вес нового контейнера: '))
count = 0
for i in stockroom:
    count += 1
    if i >= new_container:
        continue
    else:
        break
print('Номер, который получит новый контейнер:', count)