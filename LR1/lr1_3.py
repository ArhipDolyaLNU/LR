import math


x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

result = ((math.sin(x)**2 * x + (math.cos(x)**3)) / 2 * y)


print('Результат виразу - ', result)
