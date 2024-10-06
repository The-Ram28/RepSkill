# Турнир
# программа, которая выводит элементы списка только с чётными индексами

participants = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []

for index in range(len(participants)):
    if (index % 2) == 0:
        first_day.append(participants[index])

print('Первый день:', first_day)