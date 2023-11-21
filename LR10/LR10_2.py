def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Знаходження всіх тризначних простих чисел
for number in range(100, 1000):
    if is_prime(number):
        print(number)
