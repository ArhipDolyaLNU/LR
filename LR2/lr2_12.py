import math


# Введення координат точок
a1 = float(input("Введіть координату a1: "))
b1 = float(input("Введіть координату b1: "))
a2 = float(input("Введіть координату a2: "))
b2 = float(input("Введіть координату b2: "))
a3 = float(input("Введіть координату a3: "))
b3 = float(input("Введіть координату b3: "))

# Обчислення відстаней від кожної точки до початку координат
distance1 = math.sqrt(a1**2 + b1**2)
distance2 = math.sqrt(a2**2 + b2**2)
distance3 = math.sqrt(a3**2 + b3**2)

# Порівняння відстаней і визначення найближчої точки
if distance1 < distance2 and distance1 < distance3:
    nearest_point = "A"
elif distance2 < distance1 and distance2 < distance3:
    nearest_point = "B"
else:
    nearest_point = "C"


print(f"Точка {nearest_point} найближча до початку координат.")
