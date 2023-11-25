def sieve_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)

    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    return primes


n = int(input("Введіть максимальне число для пошуку простих чисел: "))
prime_set = set(sieve_eratosthenes(n))
print("Множина простих чисел до", n, ":", prime_set)
