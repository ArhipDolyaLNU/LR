import math

# Введення значення x
x = float(input("Введіть значення x: "))

# Обчислення кореня з 3
sqrt_of_3 = math.sqrt(3)

# Обчислення виразу
result = sqrt_of_3 * x * (math.sin(1 / x)) + 1.57

# Виведення результату
print("Результат обчислення виразу: ", result)
