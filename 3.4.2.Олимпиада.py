# Олимпиада
# программу, которая принимает на вход количество участников и количество человек в каждой
# команде, за-тем генерирует список таких команд и выводит его на экран.

participants = []
participants_num = int(input('Количество участников: '))
team_num = int(input('Количество человек в команде: '))
if participants_num % team_num > 0:
    print(f'{participants_num} участников невозможно поделить на команды по {team_num} человек!')
else:
    num = 1
    for _ in range(participants_num // team_num):
        team = list(range(num, num + team_num))
        participants.append(team)
        num += team_num
    print('Общий список команд:', participants)
