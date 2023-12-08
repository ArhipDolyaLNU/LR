# lambda-функція для обчислення факторіалу
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Виклик лямбда-функції для знаходження факторіалу числа 5
result = factorial(5)

print(f"Факторіал числа 5: {result}")
