eps = 0.0001
x_values = [-1, 0, 1]

for x in x_values:
    result = 0
    term = x
    n = 1

    while abs(term) > eps:
        result += term
        n += 1
        term = (-1) ** (n - 1) * (x ** (2 * n - 1)) / (2 * n - 1)

    print(f'arctan({x}) = {result}')