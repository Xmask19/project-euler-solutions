"""
Project Euler Problem 2: Even Fibonacci Numbers

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

fib1 = 1
fib2 = 2

total = 2

while fib1 < 4e6 and fib2 < 4e6:
    fib1 += fib2
    if fib1 % 2 == 0 and fib1 < 4e6:
        total += fib1
    fib2 += fib1
    if fib2 % 2 == 0 and fib2 < 4e6:
        total += fib2

print(total)
