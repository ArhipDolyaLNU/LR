def arctg1(x, epsilon):
    result = 0  # Початкове значення суми
    n = 0       # Лічильник

    term = x  # Початковий доданок

    while abs(term) >= epsilon:
        result += term
        n += 1
        term = (-1) ** n * (x ** (2 * n + 1)) / (2 * n + 1)

    return result


x = float(input("Введіть значення x (|x| < 1): "))
epsilon = float(input("Введіть допустиму похибку ε (> 0): "))


# Перевірка, чи виконані обмеження |x| < 1 та ε > 0
if abs(x) >= 1 or epsilon <= 0:
    print("Обмеження не виконані.")
else:
    arctg_x = arctg1(x, epsilon)
    print(f"arctg({x}) = {arctg_x}")
