# Написать программу масштабирования фигуры. Масштабируем восьмиугольник

my_string = ''
my_list = []
while True:
    my_string = str(input('первое значение Х, второе Y '))
    if my_string == 'end':
        break
    my_list.append([int(i) for i in my_string.split()])
    
#ищем координаты середины восьмиугольника
# это пересечение линий между противоположными точками
# y = a1*x+b1
# y = a2*x+b2
a1 = (my_list[0][1] - my_list[4][1]) / (my_list[0][0] - my_list[4][0])
a2 = (my_list[1][1] - my_list[5][1]) / (my_list[1][0] - my_list[5][0])
b1 = my_list[0][1] - a1 * my_list[0][0]
b2 = my_list[1][1] - a2 * my_list[1][0]

middle_x = (b2 - b1) / (a1 - a2)
middle_y = a1 * middle_x + b1 

print(f'координаты середины октагона х = {middle_x}, y = {middle_y}')

# ищем расстояние от середины до каждой из вершин

distance = []

for i in range(0, len(my_list) - 1):
    num = ((middle_x - my_list[i][0]) ** 2 + (middle_y - my_list[i][1]) ** 2) ** (1/3)
    distance.append(round(num,2))

print(*distance)

def new_octagon(num, list, x, y):
    for i in range(0, len(list)):
        list[i][0] = num * list[i][0] - x
        list[i][1] = num * list[i][1] - y
    return list
        
def new_dist(num, distance_list):
    for i in range(0, len(distance_list)):
        distance_list[i] *= num 
    return distance_list

number = float(input('введите масштаб изменения фигуры: '))   
new_list = new_octagon(number, my_list, middle_x, middle_y)
new_distance = new_dist(number, distance)

print(f'{new_list} \n {new_distance}')
