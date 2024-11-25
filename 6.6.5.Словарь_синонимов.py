# Задание 5. Словарь синонимов
# Реализуйте код, который составляет словарь синонимов (все слова в словаре различны), затем запрашивает
# у пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода: если такого слова нет,
# выведите ошибку и запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов.

num = int(input('Введите количество слов: '))

synonym_dict = dict()

for i in range(num):
    print('{0}-я пара:'.format(i + 1), end=' ')
    word = input().lower().split(' - ')
    synonym_dict[word[0]] = word[1]
while True:
    request = input('Введите слово: ').lower()
    if request in synonym_dict.keys():
        print('Синоним:', synonym_dict[request].title())
        break
    elif request in synonym_dict.values():
        for i in synonym_dict:
            if synonym_dict[i] == request:
                print('Синоним:', i.title())
        break
    else:
        print('Такого слова в словаре нет.')