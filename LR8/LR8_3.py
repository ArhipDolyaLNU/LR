input_string = input("Введіть рядок: ")

clean_string = ''

for char in input_string:
    if char not in clean_string:
        clean_string += char

print(clean_string)