# Недоделка (12.6 зад 7)

def rock_paper_scissors(number):
    word = int(
        input('Ваш выбор: Камень (1), Ножницы (2), Бумага (3), Выход (4): '))
    answer = ''
    if word == 1:
        number += 3
    elif word == 2:
        number += 6
    elif word == 3:
        number += 9
    elif word == 4:
        print('Спасибо за игру. До встречи')
        mainMenu()
    elif word == 0 or word > 4:
        print('Введите "1", "2", "3" или "4"')
    x = (number + word) * 3 % 10
    if x < 4:
        answer = 'камень'
    elif x >= 7:
        answer = 'ножницы'
    else:
        answer = 'бумага'
    if (answer == 'камень' and word == 1) or (answer == 'ножницы' and word == 2) or (answer == 'бумага' and word == 3):
        print(answer, 'n\ Ничья!')
    elif (answer == 'камень' and word == 2) or (answer == 'ножницы' and word == 3) or (answer == 'бумага' and word == 1):
        print(answer, 'n\ Я победил!')
    elif (answer == 'камень' and word == 3) or (answer == 'ножницы' and word == 1) or (answer == 'бумага' and word == 2):
        print(answer, 'n\ Я проиграл!')
    rock_paper_scissors(number)


def guess_the_number(a, b):
    number = b // 2
    while True:
        print(f'Ваше число {number}?', end='\n')
        answer = int(
            input('Если ДА -> 1, если больше -> 2, если меньше -> 3: '))
        if answer == 2:
            a = number
            number = (a + b) // 2
        elif answer == 3:
            b = number
            number = (a + b) // 2
        elif answer == 1:
            print('Я угадал! Спасибо за игру')
            mainMenu()
        else:
            print('Ответьте не корректен')


def mainMenu():
    choice = int(input(
        'Выбери игру: «Камень, ножницы, бумага» нажми - 1, «Угадай число» нажми - 2: '))
    if choice == 1:
        print("Добро пожаловать в игру «Камень, ножницы, бумага»")
        rock_paper_scissors(55)
    elif choice == 2:
        print("Добро пожаловать в игру «Угадай число!»")
        print('Выберите число от 1 до 500')
        guess_the_number(1, 500)
    else:
        print('Ошибка в выборе!')
        mainMenu()


print('Добро пожаловать!')
mainMenu()
