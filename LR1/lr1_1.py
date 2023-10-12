import math


x1 = float(input("Введіть x1: "))
y1 = float(input("Введіть y1: "))
x2 = float(input("Введіть x2: "))
y2 = float(input("Введіть y2: "))
x3 = float(input("Введіть x3: "))
y3 = float(input("Введіть y3: "))


a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))


print('Площа трикутника - ', area)