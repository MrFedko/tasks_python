import random

def fill(any):
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            any[i][j] = random.randint(1, 9)
    return any

def print_ar(any):
    for i in any:
        print(i)  
