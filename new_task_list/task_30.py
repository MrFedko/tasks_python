# Вычислить число pi c заданной точностью d
# Пример: при d = 0.001, pi = 3.141   
# 10^-1 <= d <= 10^-10

from math import pi

d = float(input('Задайте точность числа пи: '))
my_pi = lambda x: pi//x*x

print(my_pi(d))




# import sys
# import math
# from decimal import *
# from math import factorial, pi
# from time import time
# from xml.etree.ElementTree import PI

# def chudnovsky(n):
#     pi = Decimal(13591409)
#     ak = Decimal(1)
#     k = 1
#     while k < n:
#         ak *= -Decimal((6*k-5)*(2*k-1)*(6*k-1))/Decimal(k*k*k*26680*640320*640320)

#         val = ak*(13591409 + 545140134*k)
#         pi += val
#         k += 1
#     pi = pi * Decimal(10005).sqrt()/4270934400
#     pi = pi**(-1)
#     return pi

# print ()
# start = time()
# my_pi = chudnovsky(10000/14)
# print ("Pi = {}".format(str(my_pi)))
# print("Time", time()-start)