def has_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'а', 'е', 'и', 'о', 'у'}
    input_string = input_string.lower()  # Перетворимо весь рядок до нижнього регістру для порівняння

    for char in input_string:
        if char in vowels:
            return True  # Якщо знайдено голосну букву, повертаємо True

    return False  # Якщо не знайдено жодної голосної букви, повертаємо False


input_string = input("Введіть рядок: ")

if has_vowels(input_string):
    print("У рядку є голосні букви.")
else:
    print("У рядку немає голосних букв.")
