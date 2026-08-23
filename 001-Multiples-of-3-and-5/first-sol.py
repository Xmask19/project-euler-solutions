"""
Project Euler Problem 1: Multiples of 3 and 5

Find the sum of all the multiples of 3 or 5 below 1000.
"""

total = 0

for i in range(1000):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i

print(total)
# 233168
