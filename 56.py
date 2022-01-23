# Написать программу, которая обменивает элементы первой строки и последней строки

import random
from all_def import fill, print_ar

m = 4
array = [[0 for i in range(0, m)] for j in range(0, m)]

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