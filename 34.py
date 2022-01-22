# Написать программу замену элементов массива на противоположные
import random
array = []

for i in range(1, 13):
    array.append(random.randint(-9, 9))
    
print(array)   

for i in range(0, len(array)):
    if array[i] < 0:
        array[i] = abs(array[i])
    else:
        array[i] = array[i] * -1
        
print(array)