# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

def search_uniq(any_list):
    new_dict = {}
    new_list = []
    for i in any_list:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
    for key, value in new_dict.items():
        if value == 1:
            new_list.append(key)
    return new_list

print(search_uniq(my_list))