# Соседи
# программу, которая выводит соседей этого символа и сообщение о количестве
# таких же символов среди этих соседей

string = input('Введите строку: ')
number = int(input('Номер символа: '))
string_list = list(string)
symbol = string_list[number - 1]
symbol_left = string_list[number - 2]
symbol_right = string_list[number]
print('\nСимвол слева:', symbol_left)
print('Символ справа:', symbol_right)
if symbol == symbol_right and symbol == symbol_left:
    print('\nЕсть ровно два такой же символа.')
elif symbol != symbol_right and symbol != symbol_left:
    print('\nТаких же символов нет.')
else:
    print('\nЕсть ровно один такой же символ.')