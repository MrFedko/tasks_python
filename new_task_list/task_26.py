# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
#  Т е для k = 5, список будет выглядеть так: [5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5]

n = int(input('введите натуральное число: '))


def fibo(number: int):
    fib =[0, 1]
    for i in range(1, number):
        fib.append(fib[i] + fib[i - 1])
    return fib

def minus_fibo(number: int):
    fib =[0, 1]
    for i in range(1, number):
        fib.append(fib[i - 1] - fib[i])
    fib.remove(0)
    fib.reverse()
    return fib
       
my_list = fibo(n)
my_new_list = minus_fibo(n)
my_new_list.extend(my_list)
print(my_new_list)

