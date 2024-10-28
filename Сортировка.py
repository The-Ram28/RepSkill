# Сортировка
# программа, которая сортирует элементы списка по возрастанию и выводит их на экран
def selection_sort(numbers):
    for i_mn in range(len(numbers)):
        for curr in range(i_mn, len(numbers)):
            if numbers[curr] < numbers[i_mn]:
                numbers[curr], numbers[i_mn] = numbers[i_mn], numbers[curr]


nums = [4, 9, 7, 6, 3, 2]
selection_sort(nums)
print((nums))