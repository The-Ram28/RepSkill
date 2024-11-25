# Задание 4. Гистограмма частоты — 2

# По итогу нужно реализовать следующие подзадачи:
# 1.	получить текст и создать из него оригинальный словарь частот;
# 2.	создать новый словарь и заполнить его данными из оригинального словаря частот, используя
# количество повторов в качестве ключей, а буквы — в качестве значений, добавляя их в список для хранения.


def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


def invert(dictionary):
    invert_dict = {}
    for i in dictionary:
        if not dictionary[i] in invert_dict:
            invert_dict[dictionary[i]] = []
        invert_dict[dictionary[i]].append(i)

    return invert_dict


text = input('Введите текст: ').lower()
hist = histogram(text)

print('Оригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, '-', hist[i_sym])

invert_hist = invert(hist)

print('Инвертированный  словарь частот:')
for i in sorted(invert_hist.keys()):
    print(i, ':', invert_hist[i])