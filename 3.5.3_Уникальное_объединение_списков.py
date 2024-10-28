# Задание 2. Уникальное объединение списков
# Напишите программу, которая объединяет два отсортированных списка целых чисел в один отсортированный
# список без дубликатов.

def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    for i_mn in range(len(list1)):
        for curr in range(i_mn, len(list1)):
            if list1[curr] < list1[i_mn]:
                list1[curr], list1[i_mn] = list1[i_mn], list1[curr]
    for i_num in list1:
        if list1.count(i_num) > 1:
            for num in range(list1.count(i_num) - 1):
                list1.remove(i_num)
    return list1


list1 = [2, 2, 2, 2, 2, 2]
list2 = [2, 2, 4, 5, 4, 6, 8, 4, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)