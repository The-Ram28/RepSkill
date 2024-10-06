# Сортировка
# программа, которая сортирует элементы списка по возрастанию и выводит их на экран

numbers = [10, 8, 6, 4, 2, 0]
for _ in range(len(numbers)):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            save = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = save

print((numbers))