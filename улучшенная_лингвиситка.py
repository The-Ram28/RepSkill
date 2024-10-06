# Улучшенная лингвистика
# программ, которая посчитает, сколько раз слова пользователя встречаются в тексте

word_list = []
word_count = [0, 0, 0]
for i in range(3):
    print(f'Введите {i + 1} слово:', end=' ')
    word = input('')
    word_list.append(word)

word_text = input('\nСлово из текста: ')
while word_text != 'end':
    for index in range(3):
        if word_list[index] == word_text:
            word_count[index] += 1
    word_text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте')
for num in range(3):
    print(word_list[num], '=', word_count[num])



