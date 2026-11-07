def array_rotation_detector(arr1: list, arr2: list) -> bool:

    if len(arr1) != len(arr2):
        return False

    str1 = ' '.join(map(str, arr1))
    str2 = ' '.join(map(str, arr2))

    return str2 in (str1 + ' ' + str1)


print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
