def factorial(num):
    if num < 0:
        return "Факторіал визначений тільки для невід'ємних цілих чисел."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


# Введення n та m з клавіатури
n = int(input("Введіть n: "))
m = int(input("Введіть m: "))


n_factorial = factorial(n)
m_factorial = factorial(m)
nm_factorial = factorial(n - m)

Cnm = n_factorial / (m_factorial * nm_factorial)
print(f"C({n}, {m}) = {Cnm}")
