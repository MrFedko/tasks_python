# Показать четные числа от 1 до N
import random
num = random.randint(1, 20)

for i in range(2, num, 2):
    print(i)