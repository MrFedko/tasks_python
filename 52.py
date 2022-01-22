# В двумерном массиве заменить элементы, у которых оба индекса чётные на их квадраты

import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = random.randint(1, 99)
        

for i in range(0, m, 2):
    for j in range(0, n, 2):
        array[j][i] **= 2
 
        
for i in array:
    print(i)