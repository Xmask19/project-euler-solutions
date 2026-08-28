def is_palindrome(n: int, b: int = 10) -> bool:
    """Return True if the representation of n in base b is a palindrome
    Args:
        n: non-negative int
        b: a base b>2, defaulting to 10

    Returns:
        True if the base-b digits of n form a palindrome
    """
    if n < 0:
        return False
    if n == 0:
        return True

    digits = []
    while n > 0:
        digits.append(n % b)
        n //= b

    left = 0
    right = len(digits) - 1
    while left < right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1
    return True


def largest_palindrome(n: int, b: int = 10) -> int:
    """Returns the largest palindrome product in base b that is
    the factor i and j, each less than n

    Args:
        n : The limit for the largest either factor can be
        b : The base in which the numbers should be considered to be 
        palindromes or not

    Returns: The largest found palindrome"""
    if b < 2:
        raise ValueError("b must be an integer at least 2")

    if n < 1:
        raise ValueError("n must be positive")

    largest = 0
    for i in range(n-1, 0, -1):
        if i * i <= largest:
            break
        for j in range(i, 0, -1):
            if i * j <= largest:
                break

            if is_palindrome(i * j, b):
                largest = i * j
                break
    return largest


if __name__ == "__main__":
    print(largest_palindrome(1000))
