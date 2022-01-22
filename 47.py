# Написать программу копирования массива
import random
array = []

for i in range(1, 13):
    array.append(random.randint(-9, 9))
      
new_array = []

new_array.append([i for i in array])

print(f'{array} \n{new_array}')