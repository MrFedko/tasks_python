# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности. 
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

def new_list(any_list):
    my_set = frozenset(any_list)
    new_list =[]
    for i in my_set:
        new_list.append(i)
    return new_list

print(*new_list(my_list))
