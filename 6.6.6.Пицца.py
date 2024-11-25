# Задание 6. Пицца
# На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида «Покупатель — название
# пиццы — количество заказанных пицц». Реализуйте код, который выводит список покупателей и их заказов по алфавиту.
# Учитывайте, что один человек может заказать одну и ту же пиццу несколько раз.

number = int(input('Введите количество заказов: '))
order_dict = {}
for num in range(number):
    order: list[str] = input('{0}-й заказ: '.format(num + 1)).split()
    order_pizza = {}
    order_pizza[order[1]] = int(order[2])
    if order[0] in order_dict:
        if order[1] in order_dict[order[0]]:
            order_dict[order[0]][order[1]] += order_pizza[order[1]]
        else:
            order_dict[order[0]][order[1]] = int(order[2])
    else:
        order_dict[order[0]] = order_pizza

for i_dict in sorted(order_dict.keys()):
    print(i_dict,':')
    for i in sorted(order_dict[i_dict].keys()):
        print(i, ':', order_dict[i_dict][i])
