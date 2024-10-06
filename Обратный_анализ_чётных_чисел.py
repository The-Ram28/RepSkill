# Обратный анализ чётных чисел
# программу, которая считывает целые числа из списка и выводит из него только чётные в обратном порядке.
# Создавать дополнительные списки нельзя
numbers = []
num = int(input('Введите количество чисел: '))
for n in range(num):
    number = int(input('введите число: '))
    numbers.append(number)

print(numbers)
for _ in range(len(numbers)):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            save = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = save
print(numbers)
x = 0
for index in range(0, len(numbers)):
    if numbers[index - x] % 2 != 0:
        del numbers[index - x]
        x += 1


print(numbers)
length = len(numbers) // 2
for num in range(1, length + 1):
    cash = numbers[num - 1]
    numbers[num - 1] = numbers[-num]
    numbers[-num] = cash
print(numbers)