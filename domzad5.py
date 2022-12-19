ax = float(input('Введите координаты точки A по оси x:'))
ay = float(input('Введите координаты точки A по оси y:'))
bx = float(input('Введите координаты точки B по оси x:'))
by = float(input('Введите координаты точки B по оси y:'))


import math
rast = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между A и B = {rast}' )