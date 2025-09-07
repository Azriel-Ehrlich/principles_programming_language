# Azriel Ehrlich 213662539
# principles of programming languages - ex1.4

# ------------------- part a ---------------------------------------
def is_prime(n,sieve):
    """Return True if n is a prime number using Eratosthenes's method."""
    if n <= 1:
        return False
    return n in sieve

def napa(n):
    """Return Eratosthenes's method of checking for prime."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return list(filter(lambda x: sieve[x], range(n + 1)))

# ------------------- part b ---------------------------------------
def has_twin_prime(n, sieve):
    """ return the twin prime if exists"""
    if not is_prime(n, sieve):
        return None
    if is_prime(n - 2, sieve):
        return n-2
    elif is_prime(n + 2, sieve):
        return n+2
    else:
        return None
    
def main():
    s = input("enter prime number:")
    try:
        n = int(s)
    except ValueError:
        print("invalid input")
        return
    sieve = napa(n + 2)
    twin = has_twin_prime(n, sieve)
    if twin:
        print(twin)
    else:
        print("invalid input")
# if __name__ == "__main__":
#     main()

# ------------------- part c ---------------------------------------
def twins_up_to(n):
    """Return a dictionary of twin primes up to n where the key is the smaller prime."""
    sieve = napa(n)
    # filter only the smaller primes of the twin pairs
    twin_pairs = filter(lambda p: p + 2 in sieve, sieve)
    # create a dictionary from the twin pairs
    return dict(map(lambda p: (p, p + 2), twin_pairs))

# example of twin primes up to 100
print(twins_up_to(100))