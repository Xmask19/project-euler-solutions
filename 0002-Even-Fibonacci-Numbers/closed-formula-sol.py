"""
Using the formula for the partial sum of the even fibonacci numbers,
a(n)= (F(3n+2-1)/2)
https://oeis.org/A099919

and Binet's formula for the fibonacci numbers
F_n = (phi^n - (1-phi)^n) / sqrt(5)

https://oeis.org/A000045
"""


import math

LIMIT = 4_000_000

sqrt5 = math.sqrt(5)
phi = (1 + sqrt5) / 2


def fib_closed(n: int) -> int:
    """Return the n-th Fibonacci number using Binet's formula."""
    return round((phi**n - (1 - phi)**n) / sqrt5)


n = int(math.log(LIMIT * sqrt5) / (3 * math.log(phi)))


if fib_closed(3 * (n + 1)) <= LIMIT:
    n += 1
elif fib_closed(3 * n) > LIMIT:
    n -= 1

answer = (fib_closed(3 * n + 2) - 1) // 2

print(answer)  # 4613732
