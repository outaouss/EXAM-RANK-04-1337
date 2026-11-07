def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped is False:
            break
    return arr


bubbleSort([0, 22, 8, 9])


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    if len(lists) == 1:
        return bubbleSort(lists[0])
    res = ""

    for i, li in enumerate(lists, start=0):
        res += ' '.join(map(str, li))
        try:
            lists[i + 1]
            res += ' '
        except IndexError:
            pass

    output = [int(c) for c in res.split() if c != '']

    return bubbleSort(output)


print(merge_sorted_lists([[15, 22, 33], [10, 9, 5], [10]]))
