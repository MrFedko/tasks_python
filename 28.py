# Подсчитать сумму цифр в числе

import random
num = random.randint(300, 9999)
print(num)
result = 0

while num != 0:
    result += num % 10
    num //= 10
    
print(result)