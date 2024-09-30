def formula(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10

# поиск глубины при помощи половинного деления


def calculate_safe_depth(danger_lvl):
    min_depth = 0
    max_depth = 4
    result = (min_depth + max_depth) / 2

    # поиск до тех пор пока не удовлетворит заданной точности
    while abs(formula(result)) >= danger_lvl:
        # какой из сторон точнее, т.е. ближе к 0
        if abs(formula(min_depth)) < abs(formula(max_depth)):
            max_depth = result
        else:
            min_depth = result

        result = (min_depth + max_depth) / 2
    return result


def main_function():
    accept_danger_lvl = float(
        input('Введите максимально допустимый уровень опасности: '))
    result = calculate_safe_depth(accept_danger_lvl)
    print('Приблизительная глубина безопасной кладки: ', result, 'm')


main_function()
