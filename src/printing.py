HELLO_TEXT = "Привет!\nЭто крестики нолики!"
SPLIT_LINE = "-------------\n"


def print_hello() -> None:
    print(HELLO_TEXT)


def print_field(field: list[list[str]]) -> None:
    field_str = SPLIT_LINE
    for row in field:
        field_str += "| "
        for item in row:
            field_str += item + " | "
        field_str += "\n" + SPLIT_LINE
    print(field_str)
