# Задача 3. Поиск элемента
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран.

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

def search(structure, key):
    if key in structure:
        return structure[key]

    for sub_structure in structure.values():
        if isinstance(sub_structure, dict):
            result = search(sub_structure, key)
            if result:
                break
    else:
        result = None

    return result


user_key = input('Искомый ключ: ')
value = search(site, user_key)
if value:
    print(value)
else:
    print('Такого ключа в структуре сайта нет.')
