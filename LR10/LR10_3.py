array = [12, 43, 2, 435, 3, 1000]
max_element = -float('inf')
index = -1

for i in range(len(array)):
    if array[i] > max_element:
        max_element = array[i]
        index = i

print(f'Максимальний елемент: {max_element} Індекс: {index}')