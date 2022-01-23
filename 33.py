# Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива

import random
array = []
for i in range(1, 13):
    array.append(random.randint(-9, 9))
    
def summ_array(any):
    result_min = 0
    result_plus = 0
    for i in any:
        if i < 0:
            result_min += i
        else:
            result_plus += i
    return result_min, result_plus

print(array, summ_array(array))