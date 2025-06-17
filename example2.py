def step(
    number: int,
    s: int,
    as_string: bool = False,
    double: bool = False,
) -> int | str:
    res = number**s
    if double:
        res *= 2
    if as_string:
        res = str(res)
    return res


res = step(5, 2, double=True)
print([res])

print(55)
print(12, end=" ")
print(13, end=" ")
print(14)
