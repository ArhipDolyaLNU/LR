def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


# Введення значень x та y
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

# Обчислення c = sign(x) + sign(y)
c = sign(x) + sign(y)

# Виведення результату
print(f"c = {c}")
