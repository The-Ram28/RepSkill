# Задача 3. Разделители символов
# Напишите программу, которая запрашивает у пользователя:
# Шаблон поздравления (туда вставляется ФИ и возраст)
# ФИ людей (в одну строку, разделяются запятой)
# Возраст каждого человека (в одну строку через пробел)
# В конце  программа выводит поздравления и всех именинников в одну строку вместе с их возрастом.


sample = input(
    'Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: '
)

name_list = input('Введите фамилии и имена через запятую: ').split(', ')
age_list = input('Введите возрасты через пробел: ').split()

for i in range(len(name_list)):
    print(sample.format(name = name_list[i], age = age_list[i]))

birthday_boys = [
    ' '.join([name_list[i_man], age_list[i_man]])
    for i_man in range(len(name_list))
]
birthday_boys_str = ', '.join(birthday_boys)
print(birthday_boys_str)