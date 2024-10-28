# Задача 3. Повышение цен
# Напишите программу, которая получает на вход список цен на товары (вещественные числа, список генерируется
# также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год.

def percent(percent, price):
    return price * (1 + percent / 100)


price_list = [float(input('Цена на товар: ')) for _ in range(5)]
percent_first = int(input('Повышение на первый год: '))
percent_second = int(input('Повышение на второй год: '))
price_first = [percent(percent_first, i_price) for i_price in price_list]
price_second = [percent(percent_second, i_price) for i_price in price_first]
print('Сумма цен за каждый год:', round(sum(price_list), 2), round(sum(price_first), 2), round(sum(price_second), 2))