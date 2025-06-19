NAMES = [
    ("Ваня", 6, 20),
    ("Петя", 7, 40),
    ("Саша", 7, 50),
]
SPLIT_LINE = "-" * 46 + "\n"


def ct(text: str | int, spaces: int, *, odd=True) -> str:
    text = str(text)
    if odd and len(text) % 2:
        text += " "
    return " " * spaces + text + " " * spaces


def format(names: list[tuple[str, int, int]]) -> str:
    text = SPLIT_LINE
    text += "|" + ct("Таблица лидеров", 14) + "|\n"
    text += SPLIT_LINE
    text += "|" + ct("Имя", 5)
    text += "|" + ct("Очки", 5)
    text += "|" + ct("Время, с", 3) + "|\n"
    text += SPLIT_LINE
    for name, points, time in NAMES:
        text += "|" + ct(name, 5)
        text += "|" + ct(points, 6)
        text += "|" + ct(time, 6) + "|\n"
    text += SPLIT_LINE

    return text


def main():
    text = format(NAMES)
    print(text)


if __name__ == "__main__":
    main()
