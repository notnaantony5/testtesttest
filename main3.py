from typing import Generator


PATH = "coord.txt"
with open(PATH, "r", encoding="utf-8") as f:
    a = f.readline()


def range2(*, end: int, start: int = 0, step: int = 1) -> Generator[int]:
    current = start
    while current < end:
        yield current
        current += step


for i in range2(start=2, step=2, end=10):
    print(i)

for i in range(2, 10, 2):
    print(i)
