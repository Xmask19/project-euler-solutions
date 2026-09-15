"""Problem 7: 10001st Prime

What is the 10001st prime number?
"""


def nth_prime(n: int) -> int:
    if n == 1:
        return 2
    else:
        primes = [2]
        k = 3
        while len(primes) < n:
            for prime in primes:
                if k % prime == 0:
                    break
            else:
                primes.append(k)
            k += 2
    return primes[-1]


if __name__ == "__main__":
    print(nth_prime(10001))
