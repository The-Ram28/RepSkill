# Анализ слова — 2
# программа, с помощью которой можно определять палиндромы
word = input('Введите слово: ')
word_list = list(word)
answer = True
for i in range(1, len(word_list) + 1):
    if word_list[i - 1] != word_list[-i]:
        print('Слово не является палиндромом')
        answer = False
        break
if answer == True:
    print('Слово является палиндромом')