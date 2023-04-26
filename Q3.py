def sieve_of_eratosthenes(numbers):

    primes = []
    sieve = [True] * (max(numbers) + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(len(sieve) ** 0.5) + 1):
        if sieve[i]:
            for j in range(i ** 2, len(sieve), i):
                sieve[j] = False
    for num in numbers:
        if sieve[num]:
            primes.append(num)
    return primes

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = sieve_of_eratosthenes(numbers)
print(primes)

