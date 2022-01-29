# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

import random 


def new_list(number):
    my_list = [1, ]
    for i in range(2, number + 1):
        my_list.append(my_list[i - 2] * i)
    return my_list

n = random.randint(2, 10)
print(n)
print(new_list(n))
    