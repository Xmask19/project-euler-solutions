"""
Generalised solution to Project Euler Problem 1.

Given a list of divisors and a limit, return the sum of all numbers
below the limit that are divisible by at least one of the divisors.

Example:
    >>> sum_multiples([3, 5], 1000)
    233168
"""


def sum_multiples(dividers: list, limit: int) -> int:
    """
    Return the sum of all multiples of any given divisor below the limit.
    Raises:
        TypeError: If dividers is not a list or if values are not integers.
        ValueError: If limit is negative or if any divisor is zero or negative.
    """

    # 1. Check that limit is an integer and non-negative
    if not isinstance(limit, int):
        raise TypeError(
            f"limit must be an integer, got {type(limit).__name__}"
            )
    if limit < 0:
        raise ValueError(
            "limit must be a non-negative integer")

    # 2. Check that dividers is a list
    if not isinstance(dividers, list):
        raise TypeError(
            f"dividers must be a list, got {type(dividers).__name__}")

    # 3. Check that all items in dividers are integers and non-zero
    for d in dividers:
        if not isinstance(d, int):
            raise TypeError(
                f"each divisor must be an integer, got {type(d).__name__}")
        if d == 0:
            raise ValueError("divisors cannot be zero")
        if d < 0:
            raise ValueError("divisors cannot be negative")

    total = 0
    for i in range(limit):
        if any(i % divisor == 0 for divisor in dividers):
            total += i
    return total


if __name__ == "__main__":
    print(sum_multiples([3, 5], 1000))  # 233168
