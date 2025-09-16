
def generate_primes():
    yield 2
    primes = [2]
    n = 3
    while True:
        limit = n**0.5
        # Check if n is prime
        if all(n % p for p in primes if p <= limit):
            primes.append(n)
            yield n
        n += 2

g = generate_primes()
for i in range(1, 100):
    print(next(g))