def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

    if not nums or k <= 0 or k > len(nums):
        return []

    res = []

    for i, _ in enumerate(nums):
        if len(nums[i: i + k]) == k:
            res.append(max(nums[i: i + k]))

    return res


print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
