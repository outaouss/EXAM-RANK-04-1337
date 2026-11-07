def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    if len(lists) == 1:
        return sorted(lists[0])

    result = []
    for li in lists:
        result.append(" ".join(map(str, li)))

    output = []
    for list in result:
        for c in list.split():
            if c:
                output.append(int(c))

    return sorted(output)


print(merge_sorted_lists([[15, 9, 33], [99, 6, 0, 15]]))
