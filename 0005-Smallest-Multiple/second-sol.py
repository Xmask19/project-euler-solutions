"""A solution to problem 5 generalised for any particular n. The primes are
generated and their greatest power less than n is found, and the smallest
number evenly divisible by all numbers less than n is found by multiplying
together these prime powers. """


from collections import defaultdict


def evenly_divisible_of_range(n: int) -> int:
    factorisation = defaultdict(int)

    primes = [2]
    x = n
    while x >= 2:
        x //= 2
        factorisation[2] += 1

    d = 3
    while n >= d:
        for prime in primes:
            if d % prime == 0:
                break
        else:
            primes.append(d)
            x = n
            while x >= d:
                x //= d
                factorisation[d] += 1
        d += 2

    prod = 1

    for key, val in factorisation.items():
        prod *= (key ** val)
    return prod


if __name__ == "__main__":
    print(evenly_divisible_of_range(20))
