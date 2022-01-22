# Показать вторую цифру трёхзначного числа
import random

num = random.randint(100,999)
second_num = (num%100)//10

print(f'{num} {second_num}')