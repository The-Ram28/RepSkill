# Задача 1. Текстовый редактор: возвращение

text = input('Введите строку: ')

text_list = list(text)
count_replace = 0
count = 0
corrected_text = ''
for i in text_list:
    if i == ':':
        text_list[count_replace] = ';'
        count += 1
    count_replace += 1
for index in text_list:
    corrected_text += index

print('Исправленная строка:', corrected_text)
print('Количество замен:', count)