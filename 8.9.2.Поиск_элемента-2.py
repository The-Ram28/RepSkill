# Задача 2. Поиск элемента — 2
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа
# на экран. По умолчанию уровень не задан.

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search(structure, key, max_depth=None):
    result = None
    if key in structure:
        return structure[key]
    elif max_depth == 1:
        return
    for k, value in structure.items():
        if isinstance(value, dict):
            if max_depth:
                max_depth-= 1
            result = search(value, key, max_depth)
            if result:
                return result
    return result



user_key = input('Введите искомый ключ: ').lower()
deep_quest = input('Хотите ввести максимальную глубину? Y/N: ').lower()
while True:
    if deep_quest == 'y':
        user_deep = int(input('Введите максимальную глубину: '))
        break
    elif deep_quest == 'n':
        user_deep = None
        break
    else:
        print('Ошибка! Введите Y/N.')

print('Значение ключа:', search(site, user_key, user_deep))