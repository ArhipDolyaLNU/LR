arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Використання lambda-функції для фільтрації парних елементів
# та обчислення їхнього добутку
product_of_even = lambda arr: 1 if len(arr) == 0 else arr[0] * product_of_even(arr[2:])

# Визначення масиву парних елементів
even_nums = list(filter(lambda num: num % 2 == 0, arr))

result = product_of_even(even_nums)

print(f"Добуток парних елементів у масиві: {result}")