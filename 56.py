# Написать программу, которая обменивает элементы первой строки и последней строки

import random
m = 4
array = [[0 for i in range(0, m)] for j in range(0, m)]

def fill(any):
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            any[j][i] = random.randint(1, 9)
    return any

def print_ar(any):
    for i in any:
        print(i)  

def rebase(any):
    count = any[0]
    any[0] = any[len(any) - 1]
    any[len(any) - 1] = count
    return any
        
fill(array)
print_ar(array)
rebase(array)
print()
print_ar(array)