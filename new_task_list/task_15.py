# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

import operator
from itertools import accumulate
import random 

def new_list(number):
    return list(accumulate([x for x in range(1, number + 1)], operator.mul))

n = random.randint(2, 10)
print(n)
print(new_list(n))