def is_prime(n):
    """
    Returns True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes():
    """
    Generator that yields prime numbers.
    """
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2

def main():
    """
    Runs the main program.
    """
    for i, prime in enumerate(primes()):
        print(prime)
        if i == 19:
            break

if __name__ == "__main__":
    main()
