def is_palindrome(n: int) -> bool:
    palindrome = True
    n = str(n)
    for i in range(len(n)-1):
        if n[i] != n[(len(n)-1)-i]:
            palindrome = False
    return palindrome


largest = 0
for i in range(900, 999):
    for j in range(900, 999):
        if is_palindrome(i * j):
            if i * j > largest:
                largest = i * j

print(largest)
