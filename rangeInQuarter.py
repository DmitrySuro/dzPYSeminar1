# Напишите программу, которая по заданному
# номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

numberQuarter = int(input('Insert number quarter: '))

if numberQuarter == 1:
    print('range coordintes where: x > 0 and y > 0')
elif numberQuarter == 2:
    print('range coordinates where: x > 0 and y < 0')
elif numberQuarter == 3:
    print('range coordinates where: x < 0 and y < 0')
elif numberQuarter == 4:
    print('range coordintes where: x < 0 and y > 0')
