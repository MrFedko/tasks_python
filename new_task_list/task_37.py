# Дан список чисел. Создать список в который попадают числа, описываемые возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]

my_list = [1, 5, 2, 3, 4, 6, 1, 7]

def array(any_list):
    many_arrays =[]
    for j in range(min(any_list), max(any_list)):
        new_list = [j]
        for i in range(any_list.index(j), len(any_list)):
            if any_list[i] - new_list[-1] <= new_list[-1] and any_list[i] > new_list[-1]:
                new_list.append(any_list[i])
        many_arrays.append(new_list)
    # return many_arrays
    max_array = []
    for i in many_arrays:
        if len(i) > len(max_array):
            max_array = i
    return max_array

my_new_list = array(my_list)
print(my_new_list)