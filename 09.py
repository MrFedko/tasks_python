# Показать последнюю цифру трёхзначного числа
import random

num = random.randint(100,999)

print(f'{num} {num%10}')