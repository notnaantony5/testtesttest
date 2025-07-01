def read_file(path="coord.txt") -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def get_tuple_from_str(line):
    pass


def get_lenght(line: str):
    coords = get_tuple_from_str(line)


def main():
    lines = read_file()
    info = (get_lenght(line) for line in lines)


if __name__ == "__main__":
    main()
