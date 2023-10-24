input_string = input("Введіть рядок: ")

# Ініціалізація лічильників для заголовних літер і цифр
uppercase_letters_count = 0
digits_count = 0

# Перевірка кожного символу у рядку
for char in input_string:
    if char.isupper():  # Перевірка, чи є символ заголовною літерою
        uppercase_letters_count += 1
    if char.isdigit():  # Перевірка, чи є символ цифрою
        digits_count += 1


print(f"Кількість заголовних літер: {uppercase_letters_count}")
print(f"Кількість цифр: {digits_count}")
