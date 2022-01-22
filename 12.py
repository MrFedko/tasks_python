# Удалить вторую цифру трёхзначного числа
import random
num = random.randint(100, 999)
new_num = (num//100) * 10 + num % 10

print(num, new_num)