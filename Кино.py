# Кино
# Напишите программу, которая позволяет добавлять в свой рейтинг фильмы, удалять их оттуда,
# а также вставлять на нужное пользователю место.

def is_film_exist(film, my_list):
    for i_film in my_list:
        if i_film == film:
            return True
    return False

films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
my_films = []
while True:
    print('\nВаш текущий список топ фильмов:', my_films)
    film = input('Название фильма: ')
    if is_film_exist(film, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            if is_film_exist(film, my_films):
                print('Этот фильм уже есть в вашем списке.')
            else:
                my_films.append(film)
        if command == 'удалить':
            if is_film_exist(film, my_films):
                my_films.remove(film)
            else:
                print('Такого фиильма нет в нашем рейтинге')
        if command == 'вставить':
            index = int(input('На какое место: '))
            my_films.insert(index - 1, film)
    else:
        print('Такого фильма нет на сайте')