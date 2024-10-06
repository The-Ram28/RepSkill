# Собачьи бега
# Программа меняет меняет  наибольший и наименьший элементы в списке
dogs_score_list = [583, 459, 457, 52, 4586, 452, 253, 478, 236]
print(dogs_score_list)
count = 0
min_score = dogs_score_list[0]
max_score = dogs_score_list[0]
min_score_count = 0
max_score_count = 0

for score in dogs_score_list:
    if score > max_score:
        max_score = score
        max_score_count = count
    if score < min_score:
        min_score = score
        min_score_count = count
    count += 1

dogs_score_list[min_score_count] = max_score
dogs_score_list[max_score_count] = min_score
print(dogs_score_list)