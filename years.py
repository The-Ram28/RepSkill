# Годы
#Найти в промежутке даты с 3 одинаковыми числами

def triple_digit_search(start, stop):
    for year in range(start, stop + 1):
        number = year
        first_num = year % 10
        year //= 10
        sec_num = year % 10
        year //= 10
        third_num = year % 10
        year //= 10
        fourth_num = year % 10
        if first_num == sec_num:
            if first_num == third_num or first_num == fourth_num:
                print(number)
        elif third_num == fourth_num:
            if third_num == first_num or third_num == sec_num:
                print(number)

first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))
print(f'Годы от {first_year} до {second_year} с тремя одинаковыми цифрами:')
triple_digit_search(first_year, second_year)

