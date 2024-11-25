# Задача 6. Контакты — 3
#
# Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить: добавить
# контакт или найти человека в списке контактов по фамилии.

def add():
    print('Вы выбрали добавить человека')
    new_name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())
    if new_name not in phonebook:
        phonebook[new_name] = int(input('Введите номер телефона: '))
    else:
        print('Такой человек уже есть в контактах')
    print('\nТекущий словарь контактов:', phonebook)


def search():
    print('Вы выбрали найти человека')
    search = input('Введите фамилию для поиска: ').title()
    flag = True
    for i_key, i_value in phonebook.items():
        if search in i_key:
            print(i_key[0], i_key[1], i_value)
            flag = False
    if flag:
        print('Такой фамилии в словаре контактов нет.')


phonebook = {}

while True:
    print('\nВведите номер действия:'
          '\n1. Добавить контакт.'
          '\n2. Найти человека.')
    choise = input('')
    if choise == '1':
        add()
    elif choise == '2':
        search()
    else:
        print('ошибка. Выберите вариант 1 или 2.')
