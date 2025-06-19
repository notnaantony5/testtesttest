NAMES = [
    ("Ваня", 6, 20),
    ("Петя", 7, 40),
    ("Саша", 7, 50),
]
max_len_name = 0
max_len_points = 0
max_len_time = 0
for name, points, time in NAMES:
    if len(name) >= max_len_name:
        max_len_name = len(name)
    if len(str(points)) >= max_len_points:
        max_len_points = len(str(points))
    if len(str(time)) >= max_len_time:
        max_len_time = len(str(time))
tabs_name = max_len_name // 8 + 1
tabs_points = max_len_points // 8 + 1
tabs_time = max_len_time // 8 + 1

SPLIT_LINE = "-" * (tabs_name + tabs_points + tabs_time) * 8 + "\n"


def ct(text: str | int, tabs: int, *, odd=True) -> str:
    text = str(text)
    text += "\t" * (tabs - len(text) // 8)
    return text


def format(names: list[tuple[str, int, int]]) -> str:
    text = SPLIT_LINE
    text += ct("Таблица лидеров", 0) + "\n"
    text += SPLIT_LINE
    text += ct("Имя", tabs_name)
    text += ct("Очки", tabs_points)
    text += ct("Время, с", tabs_time) + "\n"
    text += SPLIT_LINE
    for name, points, time in NAMES:
        text += ct(name, tabs_name)
        text += ct(points, tabs_points)
        text += ct(time, tabs_time) + "\n"
    text += SPLIT_LINE

    return text


def main():
    text = format(NAMES)
    print(text)


if __name__ == "__main__":
    main()
