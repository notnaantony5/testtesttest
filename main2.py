from math import sqrt
from typing import Generator


def read_file(path="coord.txt") -> Generator[str]:
    with open(path, "r", encoding="utf-8") as f:
        yield f.readline()


def get_tuple_from_str(line: str) -> tuple[int, int]:
    x, y = line.strip().split(", ")
    return int(x), int(y)


def get_lenght(line: str) -> tuple[float, tuple[int, int]]:
    x, y = get_tuple_from_str(line)
    lenght = sqrt(x**2 + y**2)
    return lenght, (x, y)


def main():
    lines_generator = read_file()
    max_lenght = 0.0
    max_coords = (0, 0)
    for lenght, coords in (get_lenght(line) for line in lines_generator):
        if lenght > max_lenght:
            max_lenght = lenght
            max_coords = coords
    print(max_coords)


if __name__ == "__main__":
    main()
