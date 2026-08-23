"""
An improvement on the generalised solution to the
"Multiples of 3 or 5" problem.

Given a list of positive integers (divisors) and a positive integer (limit),
return the sum of all numbers below the limit that are divisible by at least
one of the divisors.

Mathematical Approach:
    Uses the inclusion-exclusion principle with arithmetic series to compute
    the sum faster.

The inclusion-exclusion principle gives a way to count
the elements of the union of sets.
https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle

To find the cardinality of the union of n sets:
    1. Include the cardinalities of the sets.
    2. Exclude the cardinalities of the pairwise intersections.
    3.Include the cardinalities of the triple-wise intersections.
    4. Exclude the cardinalities of the quadruple-wise intersections.
    5. Include the cardinalities of the quintuple-wise intersections.
    6. Continue, until the cardinality of the n-tuple-wise intersection is
       included (if n is odd) or excluded (n even).




Example:
    >>> sum_multiples([3, 5], 1000)
    233168"""


from itertools import combinations
from math import lcm
from typing import List


def sum_multiples(dividers: List[int], limit: int) -> int:
    """
    Return the sum of all multiples of any given divider below the limit.

    Args:
        dividers: A list of positive integers to check divisibility against.
        limit: A non-negative integer representing the upper bound (exclusive).

    Returns:
        The sum of all integers in [0, limit)
        divisible by at least one divider.

    Raises:
        TypeError: If arguments are of the wrong type.
        ValueError: If limit is negative or a divider is zero/negative.
    """
    _validate_inputs(dividers, limit)
    if dividers == []:
        return 0
    dividers = sorted(set(dividers))  # Removes repeated dividers

    total = 0
    # For each subset of dividers, we determine whether to add or subtract
    # their sum based on the subset size. Odd include, even exclude.
    for subset_length in range(1, len(dividers) + 1):
        for combo in combinations(dividers, subset_length):
            lcm_value = lcm(*combo)
            if lcm_value < limit:
                sign = 1 if subset_length % 2 == 1 else -1
                total += sign * _sum_multiples_below(lcm_value, limit)
    return total


def _validate_inputs(dividers: List[int], limit: int) -> None:
    """
    Validate that inputs meet the expected requirements.

    Raises:
        TypeError: If arguments are of the wrong type.
        ValueError: If limit is negative or a divisor is zero/negative.
    """
    # Check limit
    if not isinstance(limit, int):
        raise TypeError(
            f"limit must be an integer, got {type(limit).__name__}")
    if limit < 0:
        raise ValueError("limit must be a non-negative integer")

    # Check dividers
    if not isinstance(dividers, list):
        raise TypeError(
            f"dividers must be a list, got {type(dividers).__name__}"
        )

    for d in dividers:
        if not isinstance(d, int):
            raise TypeError(
                f"each divisor must be an integer, got {type(d).__name__}"
            )
        if d == 0:
            raise ValueError("divisors cannot be zero")
        if d < 0:
            raise ValueError("divisors cannot be negative")


def _sum_multiples_below(step: int, limit: int) -> int:
    """
    Return the sum of all multiples of `step` below `limit`.

    Uses the arithmetic series formula.

    Example:
        >>> _sum_multiples_below(3, 10)
        18  # 3 + 6 + 9 = 18
    """
    n = (limit - 1) // step
    return step * n * (n + 1) // 2


if __name__ == "__main__":
    print(sum_multiples([3, 5], 1000))  # 233168
    print(sum_multiples([3, 5, 7, 11], 1000000000))  # 292207792292207785
