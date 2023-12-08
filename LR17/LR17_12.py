arr = [1, 2, 3, 4, 5, 6, 7, 8]
product = 1

even_arr = [i for i in arr if i % 2 == 0]

for i in even_arr:
    product *= i

print(f"Добуток парних елементів у масиві: {product}")