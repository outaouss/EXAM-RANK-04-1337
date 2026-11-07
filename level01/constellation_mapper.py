def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    if not stars:
        res = []
        for _ in range(2):
            res.append("." * dim)
        return res

    output = []
    stars_set = set(stars)
    result = []
    for r in range(dim):
        output = []
        for c in range(dim):
            if (r, c) in stars_set:
                output.append("*")
            else:
                output.append(".")
        j = ''.join(output)
        result.append(j)

    return result


print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
