from typing import Generator


INPUT_PATH = "names.txt"


def generate_lines_from_file(path: str = INPUT_PATH) -> Generator[str, None, None]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def filter_by_a(generator: Generator[str, None, None]) -> Generator[str, None, None]:
    for text in generator:
        if text.split(" ")[1].startswith("А"):
            yield text


def main():
    gen = generate_lines_from_file()
    filt = filter_by_a(gen)
    for line in filt:
        print(line)


if __name__ == "__main__":
    main()
