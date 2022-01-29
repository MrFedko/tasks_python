import random

def fill(any):
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            any[i][j] = random.randint(1, 99)
    return any

def print_ar(any):
    for i in any:
        print(i)  

def double_calc(n):
    result = ''
    while n != 0:
        result = str(n % 2) + result
        n //= 2
    return result