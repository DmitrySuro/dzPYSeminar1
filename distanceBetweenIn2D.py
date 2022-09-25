# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

aX = int(input('Insert coordinates point aX'))
aY = int(input('Insert coordinates point aY'))

bX = int(input('Insert coordinates point bX'))
bY = int(input('Insert coordinates point bY'))

distance = math.sqrt((aX - bX)**2 + (aY - bY)**2)
print(distance)
