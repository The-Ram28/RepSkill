# Задание 4. Заглавные буквы
# Напишите программу, которая меняет регистр символов в этой строке так, чтобы первая буква каждого
# слова была прописной, а остальные — строчными

string = input('Введите строку: ').split(' ')

for i in range(len(string)):
    symbols = [ i_sym for i_sym in string[i]]
    symbols[0] = symbols[0].upper()
    string[i] = ''.join(symbols)

print('Результат:', ' '.join(string))