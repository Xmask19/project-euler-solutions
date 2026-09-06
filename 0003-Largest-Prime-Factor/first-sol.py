"""
Project Euler Problem 3: Largest Prime Factor

What is the largest prime factor of the number 600851475143"""

import math
if __name__ == "__main__":
    biggest = 1
    pfactors = []
    for i in range(1, round(math.sqrt(600851475143))):
        if 600851475143 % i == 0:
            if i not in pfactors:
                pfactors.append(i)
                biggest = i

    print(pfactors)
