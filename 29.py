# Написать программу вычисления произведения чисел от 1 до N

import random
num = random.randint(1, 300)
result = 1

for i in range(1, num + 1):
    result *= i
    
print(num, result)