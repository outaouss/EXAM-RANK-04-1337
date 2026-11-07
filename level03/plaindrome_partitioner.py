def palindrome_partitioner(s: str) -> int:
    if not s or s == s[::-1]:
        return 0

    cuts = 0
    i = 0
    n = len(s)

    while i < n:
        longest_end = i
        for j in range(i, n):
            substring = s[i: j + 1]
            if substring == substring[::-1]:
                longest_end = j

        i = longest_end + 1

        if i < n:
            cuts += 1

    return cuts


print(palindrome_partitioner("aab"))
print(palindrome_partitioner("aba"))
print(palindrome_partitioner("abc"))
