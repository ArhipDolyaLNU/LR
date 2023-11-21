def factorial(num):
    if num < 0:
        return "Факторіал визначений тільки для невід'ємних цілих чисел."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


# Введення n та m
n = int(input("Введіть n: "))
m = int(input("Введіть m: "))

# Обчислення числа поєднань C(n, m)
combinations = factorial(n) // (factorial(m) * factorial(n - m))

# Виведення результату
print(f"C({n}, {m}) = {combinations}")