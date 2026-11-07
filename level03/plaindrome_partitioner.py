def palindrome_partitioner(s: str) -> int:
    # Base cases: empty string or full string is a palindrome
    if not s or s == s[::-1]:
        return 0

    cuts = 0
    i = 0
    n = len(s)

    while i < n:
        # Find the longest palindrome starting at current index i
        longest_end = i
        for j in range(i, n):
            substring = s[i: j + 1]
            if substring == substring[::-1]:
                longest_end = j

        # Jump index i past the palindrome we just found
        i = longest_end + 1

        # Increment cut count if we aren't at the end of the string yet
        if i < n:
            cuts += 1

    return cuts


print(palindrome_partitioner("aab"))
print(palindrome_partitioner("aba"))
print(palindrome_partitioner("abc"))
