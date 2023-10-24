input_string = input("Введіть рядок: ")

# Введення символу, який ви хочете підрахувати
char_to_count = input("Введіть символ, який ви хочете підрахувати: ")

# Використання методу count() для підрахунку входжень символу
frequency = 0

for char in input_string:
    if char == char_to_count:
        frequency += 1

# Виведення результату
print(f"Символ '{char_to_count}' зустрічається {frequency} разів у введеному рядку.")
