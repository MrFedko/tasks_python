# В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]

import random
array = []
count = 0

for i in range(1, 124):
    array.append(random.randint(1, 999))

for i in array:
    if i in range(10, 100):
        count += 1
        
print(count) 