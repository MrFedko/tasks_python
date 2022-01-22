# Выяснить являются ли три числа сторонами треугольника

triangle = []

for i in range(0, 3):
    triangle.append(int(input('введите значение стороны предполагаемого треугольника ')))
    
def realy_triangle(number):
    a = number[0]
    b = number[1]
    c = number[2]
    
    return (a < (b + c)) and (b < (a + c)) and (c < (a + b));

if realy_triangle(triangle):
    print(*triangle, 'являются сторонами треугольника')
else:
    print(*triangle, 'не являются сторонами треугольника')
