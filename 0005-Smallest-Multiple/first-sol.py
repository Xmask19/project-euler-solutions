"""
Project Euler Problem 5: Largest Prime Factor

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Some reasoning allows us to give the answer as the following product. For "
each prime less than 20, find the greatest power of that prime less than 20.
The product of these prime powers will be evenly divisible by all the numbers
from 1 to 20.

Consider the prime factorisation of any number less than 20. Clearly the number
divides the constructed product. Equally, any candidate that is not a multiple
of this product will be missing one of these prime power factors and the
candidate would not be a multiple of this prime power.

"""
if __name__ == "__main__":
    print(16*9*5*7*11*13*17*19)  # 232792560
