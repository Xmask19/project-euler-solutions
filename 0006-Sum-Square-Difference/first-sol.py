"""Project Euler Problem 6: Sum Square Difference
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""


def sum_square_diff(n: int) -> int:
    return round(n*n*(n+1)*(n+1)/4 - n*(n+1)*(2*n+1)/6)


if __name__ == "__main__":
    print(sum_square_diff(100))
