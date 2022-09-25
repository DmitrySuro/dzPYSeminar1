# Напишите программу, которая принимает на вход
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
#  номер четверти плоскости, в которой находится
#  эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Insert coordinate x: '))
y = int(input('Insert coordinates y: '))

if x == 0 and y == 0:
    print('your point in the middle')
elif x == 0 and y != 0:
    print('Point on axis X')
elif x != 0 and y == 0:
    print('point on axis Y')

elif x > 0 and y > 0:
    print('Point in first quarter')
elif x > 0 and y < 0:
    print('Point in second quarter')
elif x < 0 and y < 0:
    print('Point in third quarter')
else:
    print('Point in fourth quarter')


