# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. 
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('задайте натуральную степень k: '))

def random_list(num = 10):
    return [random.randint(0, 100) for i in range(num)]

def mnogochlen(number, my_list = random_list()):
    file = open('file_33_task.txt', 'w')
    file.write(f'{random.choice(my_list)}*(x**{number}) + {random.choice(my_list)}*x + {random.choice(my_list)} = 0 \
    \nx**{number} + {random.choice(my_list)} = 0 \
    \n{random.choice(my_list)}*(x**{number}) = 0')
    file.close()
    
mnogochlen(k)
    
    