#1 Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
'''
print('Введите день недели: ')
day = int(input())
if day > 7 or day <= 0:
    print('Данного дня недели не существует')
else:
    if day >= 6:
        print('Данный день недели является выходным')
    else: 
        print('Данный день недели является рабочим')
'''

#1 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) 
# = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            print ((not(x or y or z)) == ((not x) and (not y) 
            and (not z)))
'''

#2 Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
'''
print('Введите значения координат x и y')
x = int(input('x = '))
y = int(input('y = '))

if x == 0 or y == 0:
    print('Координаты не должны быть равными нулю')
else:
    if x > 0 and y > 0:
        print('Координаты лежат в 1-ой четверти')
    elif x < 0 and y > 0:
        print('Координаты лежат во 2-ой четверти')
    elif x < 0 and y < 0:
        print('Координаты лежат в 3-ой четверти')
    else:
        print('Координаты лежат в 4-ой четверти')
'''
#1 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
'''
print('Введите номер четверти ')
quarter = int(input())
if quarter <= 0 or quarter > 4:
    print('Данной четверти не существует!')
else:
    if quarter == 1:
        print('x > 0 и y > 0')
    elif quarter == 2:
        print('x < 0 и y > 0')
    elif quarter == 3:
        print('x < 0 и y < 0')
    else:
        print('x > 0 и y < 0')
'''

# Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.
'''
import math
print('Введите координаты точки A:')
x_A = int(input())
y_A = int(input())
print('Введите координаты точки B:')
x_B = int(input())
y_B = int(input())
distance = round(math.sqrt(math.pow(x_B - x_A,2) + math.pow(y_B - y_A,2)),1)
print(f'Расстояние между двух точек = {distance}')
'''