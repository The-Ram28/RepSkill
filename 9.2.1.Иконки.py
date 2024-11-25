# Задача 1. Иконки
# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь
# (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение. Если путь
# указывает на файл, то также выведите его размер (сколько он весит в байтах).

import os

def find_file(cur_path, file_name):
    print('переходим', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('   смотрим', path)

        if os.path.isdir(path):
            print('    это директория')
        if os.path.isfile(path):
            print('    Это файл')
            print(os.path.getsize(path))
        if os.path.islink(path):
            print('    это ссылка')
            result = find_file(path, file_name)



file_path = find_file(os.path.abspath
                      (os.path.join(os.path.sep, 'Ramil')),
                      'яйца.py')
