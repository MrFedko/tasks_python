# Составить частотный словарь элементов двумерного массива

import random
from all_def import fill, print_ar

m = 10
array = [[0 for i in range(0, m)] for j in range(0, m)]

def dictinary(any):
    my_dict = {}
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            if any[i][j] not in my_dict.keys():
                my_dict[any[i][j]] = 1
            else:
                my_dict[any[i][j]] += 1                
    return my_dict

            
fill(array)
print_ar(array)
result = dictinary(array)

for key,value in result.items():
    print(f'{key}: {value} - {round(value/((m * m) / 100), 2)}%')
