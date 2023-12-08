fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)


result = fibonacci(5)

print(f"Число Фібоначчі з індексом 5: {result}")
