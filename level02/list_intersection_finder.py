def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    # Edge case: if input list is empty or any sublist inside is empty
    if not lists or any(len(li) == 0 for li in lists):
        return []

    common = set(lists[0])

    for li in lists[1:]:
        common.intersection_update(li)

    return sorted(list(common))


print(list_intersection_finder([[1, 2, 3], [1, 5, 6, 2]]))
