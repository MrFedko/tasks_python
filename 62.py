# В двумерном массиве целых чисел. Удалить строку и столбец, на пересечении которых расположен наименьший элемент.

import random
from all_def import fill, print_ar

m = 5
array = [[0 for i in range(m)] for j in range(m)]

def search_position(any):
    minimum = any[0][0]
    min_pos_row = 0
    min_pos_str = 0
    for i in any:
        for j in i:
            if j < minimum:
                minimum = j
                min_pos_row = i.index(j)
                min_pos_str = any.index(i)
    return minimum, min_pos_str, min_pos_row

def delete_str_row(any, str, row):
    new_any =[[0 for i in range(len(any) - 1)] for j in range(len(any) - 1)]
    k = 0
    m = 0
    for i in range(len(any)):
        if i + 1 > len(any):
            break
        elif i == str:
            continue
        for j in range(len(any)):
            if j + 1 > len(any):
                break
            elif j == row and j + 1 <= len(any):
                continue
            new_any[k][m] = any[i][j]
            m += 1
        m = 0
        k += 1
    return new_any
            

fill(array)
min_num, min_str, min_row = search_position(array)
print_ar(array)
print(f'минимальное число - {min_num} [{min_str}][{min_row}]')
new_array = delete_str_row(array, min_str, min_row)
print_ar(new_array)
