# Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

from itertools import accumulate
import math
n = int(input('Введите сколько чисел последовательности вывести на экран: '))

def odd(_, any):
    if math.log(any, 3) % 2 != 0:
        any *= - 1
    return any

my_new_list = list(accumulate([3 ** x for x in range(n)], odd))

print(*my_new_list)