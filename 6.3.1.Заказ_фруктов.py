# Задача 1. Заказ фруктов
# Напишите программу, которая суммирует стоимость (цена × количество) всех заказанных товаров, и
# выведите итоговую сумму в консоль.

order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

sum_order = 0

for fruit in order:
    sum_order += incomes.get(fruit, 0) * order[fruit]

print('Стоимость всех заказанных товаров {0} рублей.'.format(sum_order))