# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

import time

def randomizer(n = 10):
    b = round(time.time() * 1000)
    return b % n

print(randomizer())

