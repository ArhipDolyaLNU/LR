with open('digits.txt', 'r') as file:
    sum_of_even = 0

    # Читання рядків з файлу
    lines = file.readlines()

    for i in range(len(lines)):
        # Перетворення рядка в список чисел
        numbers = []
        for num in lines[i].split():
            numbers.append(int(num))
        # Перебор чисел в списку
        for j in range(len(numbers)):
            # Перевірка, чи номер числа парний
            if (i + 1) % 2 == 0:
                sum_of_even += numbers[j]


print("Сума елементів з парними номерами:", sum_of_even)
