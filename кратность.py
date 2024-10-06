# Кратность
# 2.2
#Пользователь вводит список из N чисел и число K. Напишите код, выводящий на
# экран сумму индексов эле-ментовсписка, которые кратны K

number_list = []

N = int(input('Количество чисел в списке: '))
for num in range(N):
    print(f'Введите {num + 1} число:', end=' ')
    number = int(input())
    number_list.append(number)


divider = int(input('Введите делитель: '))
i_list = []
i_summ = 0
i_count = 0
for i in number_list:
    if i % divider == 0:
        print(f'Индекс числа {i}: {i_count}')
        i_summ += i_count
    i_count += 1

print('Сумма индексов:', i_summ)