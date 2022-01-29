# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
def my_new_list(number):
    my_list = []
    for i in range(-1 * number, number):
        my_list.append(i)
    return my_list

def my_set(file):
    my_file = open(file, 'r')
    my_list = []
    for line in my_file: 
        line = line.replace(f'\n', '')
        my_list.append(line)
    my_file.close()
    my_set = set(my_list)
    return my_set

print(my_set('file.txt'))        
n = int(input('введите чсисло n: '))


