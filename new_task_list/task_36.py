# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
my_list = [1, 3, 2, 3, 4, 6, 1, 7]

def array(any_list):
    new_list = [any_list[0]]
    for i in any_list:
        if i > new_list[-1]:
            new_list.append(i)
    return new_list

my_new_list = array(my_list)
print(my_new_list)