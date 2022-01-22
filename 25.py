# Найти сумму чисел от 1 до А

import random
num = random.randint(1, 99)
sum = 0

for i in range(1, num):
    sum += i
    
print(num, sum)