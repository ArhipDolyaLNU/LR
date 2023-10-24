# Розмірності масивів n і m
n = int(input("Введіть розмірність n: "))
m = int(input("Введіть розмірність m: "))

# Створюємо масив A і заповнюємо його
A = []
for i in range(n):
    value = int(input(f"Введіть значення для A[{i}]: "))
    A.append(value)

# Створюємо масив B і заповнюємо його
B = []
for j in range(m):
    value = int(input(f"Введіть значення для B[{j}]: "))
    B.append(value)

# Створюємо двовимірний масив D і заповнюємо його значеннями
D = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i] * B[j])
    D.append(row)

# Виводимо початковий масив D
print("Початковий масив D:")
for row in D:
    print(row)

# Обнуляємо негативні значення в масиві D
for i in range(n):
    for j in range(m):
        if D[i][j] < 0:
            D[i][j] = 0

# Виводимо оновлений масив D
print("Оновлений масив D:")
for row in D:
    print(row)
