def print_digits(n):
    if n < 10:
        print(n, end=" ")  # Друкуємо число і пробіл
    else:
        print_digits(n // 10)  # Рекурсивно викликаємо функцію для меншого числа
        print(n % 10, end=" ")  # Друкуємо останню цифру і пробіл


N = int(input("Введіть натуральне число N: "))

# Викликаємо функцію для друку цифр числа
print_digits(N)