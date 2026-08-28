import math


def miller_rabin_test(n: int) -> bool:
    """Miller-Rabin primality test.

    Write n-1 in the form d * 2 ^ s, with d odd
    n is said to be a strong probable prime to base a if one of the following
    congruence relations holds:

    a^d ≡ 1 or
    a^(d*2^r) ≡ -1 for some 0 ≤ r < s

    if n is not a strong probable prime to base any base a, it is composite.
    """
    if n < 2:
        return False
    primes_12 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # if it is one of these, it is prime, if it is a multiple, it is not
    for p in primes_12:
        if n == p:
            return True
        if n % p == 0:
            return False

    # we want to write n-1 in the form d * 2^ s, with d odd.
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # We check for each base if n is a strong probable prime
    # If it fails for any base, it is not prime
    # It is known that the miller-rabin test with the first 12 primes
    # works for 64-bit integers
    for a in primes_12:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(1, s):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            # If it is not a strong probable prime for some base, composite
            return False
    return True


def g(x: int, n: int, c: int) -> int:
    return (x * x + c) % n


def pollard_rho(n: int) -> int:
    """Return a non-trivial factor of composite n using
    Pollard's Rho algorithim."""
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    c = 1

    MAX_ATTEMPTS = 30
    MAX_STEPS = 10000
    for _ in range(MAX_ATTEMPTS):
        x = 2
        y = x
        d = 1

        for _ in range(MAX_STEPS):
            # using the floyd cycle finding algorithm to detect cycles
            x = g(x, n, c)
            y = g(g(y, n, c), n, c)
            d = math.gcd(abs(x - y), n)
            if d > 1:
                break
        if d != 1 and d != n:
            return d
        else:
            c += 1

    raise ValueError(
        f"Pollard's Rho failed to factor {n} after {MAX_ATTEMPTS} attempts")


def factor_find(n: int) -> set[int]:
    """Find the prime factors of n"""

    if n == 1:
        return set()
    if miller_rabin_test(n):
        return {n}

    d = pollard_rho(n)

    return factor_find(d) | factor_find(n // d)


def largest_prime_factor(n: int) -> int:
    """Find the largest prime factor of a positive integer n"""
    if n < 2:
        raise ValueError("n must be at least 2")
    return max(factor_find(n))


if __name__ == "__main__":
    print(largest_prime_factor(13195))
    print(largest_prime_factor(600851475143))
