import math


a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

x = a**4 + b**2

y = (math.log(x)**2) / (1 + math.sin(x)**2)

print('Значення виразу y:', y)




