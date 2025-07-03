from typing import Generator


INPUT_PATH = "names.txt"
OUTPUT_PATH = "result_names.txt"


def generate_lines_from_file(path: str = INPUT_PATH) -> Generator[str, None, None]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def filter_by_a(generator: Generator[str, None, None]) -> Generator[str, None, None]:
    for text in generator:
        if text.split(" ")[1].startswith("А"):
            yield text


def transform(generator: Generator[str, None, None]) -> Generator[str, None, None]:
    for text in generator:
        lastname, firstname = text.split(" ")
        firstname = firstname[0] + "."
        yield lastname + " " + firstname


def main():
    gen = generate_lines_from_file()
    filt = filter_by_a(gen)
    result = transform(filt)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for line in result:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
