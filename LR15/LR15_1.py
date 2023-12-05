def sieve_of_eratosthenes(n):
    # Створюємо масив розміром n
    primes = [0] * n

    # Заповнюємо масив значеннями True
    for i in range(n):
        primes[i] = True

    # Проходимо по всьому масиву від 2 до квадратного кореня з n
    for i in range(2, int(n ** 0.5) + 1):
        # Якщо число просте, відзначаємо як непрості всі його кратні
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    # Числа, що залишилися простими
    digits = []
    for i in range(n):
        if primes[i]:
            digits.append(i)

    return digits


primes = sieve_of_eratosthenes(100)
print(primes)