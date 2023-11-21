x = input("Введіть число X: ")

# Перевірка чи X є шестизначним числом
if len(x) != 6:
    print("Число не є шестизначним.")
else:
    # Розділити рядок X на список цифр
    digits = []

    for digit in x:
        digits.append(int(digit))

    # Обчислення сум перших і останніх трьох цифр
    sum_first_half = sum(digits[:3])
    sum_second_half = sum(digits[3:6])

    # Перевірка, чи суми рівні і виведення результату
    if sum_first_half == sum_second_half:
        print(f"Число {x} - є шестизначним та є щасливим.")
    else:
        print(f"Число {x} - є шестизначним, але не є щасливим.")
