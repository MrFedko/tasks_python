# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
def my_new_list(number):
    my_list = []
    for i in range(-1 * number, number + 1):
        my_list.append(int(i))
    return my_list

def my_set(file):
    my_file = open(file, 'r')
    my_list = []
    for line in my_file: 
        line = line.replace(f'\n', '')
        my_list.append(int(line))
    my_file.close()
    my_set = set(my_list)
    return my_set

def product_list(new_list, new_set):
    product = 1
    for i in range(len(new_list)):
        if i in new_set:
            product *= new_list[i]
    return product


print(my_set('file.txt'))        
n = int(input('введите чсисло n: '))
my_list = my_new_list(n)
my_new_set = my_set('file.txt')
product = product_list(my_list, my_new_set)
print(*my_list)
print(product)