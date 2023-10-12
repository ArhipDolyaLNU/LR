import math

# Змінні та константи
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))
a = 10

result = ((x + y) * (a - x)) / (math.sqrt(abs(y)) + math.sin(x))

print('Результат виразу - ', result)