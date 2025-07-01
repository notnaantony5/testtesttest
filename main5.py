from math import sqrt

print(
    max(
        (
            (sqrt(x**2 + y**2), (x, y))
            for x, y in (
                tuple(map(int, line.strip().split(", ")))
                for line in open("coord.txt", "r", encoding="utf-8")
            )
        ),
        key=lambda x: x[0],
    )[1]
)
