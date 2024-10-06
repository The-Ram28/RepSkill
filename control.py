# Контроль.
# 2.1 Кто из сотрудникоа на рабочем месте
id_employees = []
number_employees = int(input('Количество сотрудников в офисе: '))
for _ in range(number_employees):
    employee = int(input('ID сотрудника: '))
    id_employees.append(employee)

found_id = int(input('Какой ID ищем? '))
for ID in id_employees:
    if id == found_id:
        answer = 'Сотрудник на работе!'
        break
    else:
        answer = 'Сотрудник не работает!'

print(answer)