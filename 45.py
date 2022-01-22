# Показать числа Фибоначчи

num = int(input('сколько чисел Фибоначчи показать? '))
fib = [0, 1]

for i in range(1, num - 1):
    fib.append(fib[i] + fib[i - 1])
    
print(*fib)