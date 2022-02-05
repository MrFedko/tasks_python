# Напишите программу, удаляющую из текста все слова содержащие "абв".
my_text = 'Дан списабвок чисел. Создать список аб в который попадают числа, описывабваемые \
    возрастающую последовательность и содержащие максималабвьное количество элемеабвнтов.'

def eraser(any_text):
    my_list = any_text.split()
    new_text = list(filter(lambda x: 'абв' not in x, my_list))
    text = ''
    for i in new_text:
        text += i + ' ' 
    return text  
print(eraser(my_text))