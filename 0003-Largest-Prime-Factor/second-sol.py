"""A small improvement on the previous solution"""
import math


def find_largest_prime(n: int) -> int:
    "For a positive integer n, find the largest prime factor"
    if n < 2:
        raise ValueError("n must be an integer greater than or equal to 2")

    if n % 2 == 0:
        n /= 2
        while n % 2 == 0:
            n /= 2
    if n == 1:
        return 2
    d = 3
    while d < math.sqrt(n):
        if n % d == 0:
            n /= d
            while n % d == 0:
                n /= d
        d += 2
    return round(n)


print(find_largest_prime(600851475143))
