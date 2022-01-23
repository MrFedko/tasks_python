# Написать программу вычисления произведения чисел от 1 до N

import random
num = random.randint(1, 300)

def product(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
    
print(num, product(num))