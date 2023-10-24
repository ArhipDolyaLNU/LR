# Введення рядку та підрядка для пошуку
input_string = input("Введіть рядок: ")
substring_to_find = input("Введіть підрядок для пошуку: ")
replacement = input("Введіть рядок для заміни: ")

# Ініціалізація порожнього рядку для результату
result_string = ""

# Ініціалізація індексу для пошуку підрядка
index = 0

while index < len(input_string):
    # Шукаємо початковий індекс підрядка
    position = -1
    for i in range(index, len(input_string)):
        if input_string[i:i + len(substring_to_find)] == substring_to_find:
            position = i
            break

    if position == -1:
        # Якщо підрядок не знайдено, додамо решту рядку до результату і завершимо
        result_string += input_string[index:]
        break

    # Додаємо частину рядку до знайденого підрядка до результату
    result_string += input_string[index:position]

    # Додаємо заміну підрядка до результату
    result_string += replacement

    # Переміщуємо індекс після знайденого підрядка
    index = position + len(substring_to_find)

# Виведення результату
print(result_string)