# Задача 2. Поиск файла
# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, проходит
# по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.

import os

def find_file(cur_path, file_name):

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                print(result)



path = os.path.abspath(os.path.join(os.path.sep, 'Ramil'))
f_name = 'main.py'
print('Ищем в:', path)
print('Имя файла:', f_name)
print('\nНайдены следующие пути:')
file_path = find_file(path, f_name)