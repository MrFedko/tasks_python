# В двумерном массиве показать позиции числа, заданного пользователем или указать, что такого элемента нет


import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = random.randint(1, 9)
        
num = int(input('inter a number for search: '))

count = 0           
for i in range(0, m):    
    for j in range(0, n):
        if array[j][i] == num:
            print(f'{num} in [{j}][{i}] position')
            count += 1

if count == 0:
    print('not in a list')
            
        
for i in array:
    print(i)