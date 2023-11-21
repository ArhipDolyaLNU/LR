def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


# Введення значень m і n з клавіатури
m = int(input("Введіть m: "))
n = int(input("Введіть n: "))

# Виклик функції Аккермана та виведення результату
result = ackermann(m, n)
print(f"A({m}, {n}) = {result}")