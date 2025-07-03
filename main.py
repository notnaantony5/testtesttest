from typing import Generator


INPUT_PATH = "names.txt"


def generate_lines_from_file(path: str = INPUT_PATH) -> Generator[str, None, None]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def main():
    for line in generate_lines_from_file():
        print(line)


if __name__ == "__main__":
    main()
