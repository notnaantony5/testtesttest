COMBINATIONS = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
]

LETTER_MAP = {"A": 0, "B": 1, "C": 2}
NUMBER_MAP = {"1": 0, "2": 1, "3": 2}


def generate_field():
    field = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    return field


def tranform_coord_to_index(coords: tuple[str, str]) -> tuple[int, int]:
    lcoord, ncoord = coords
    return LETTER_MAP[lcoord], NUMBER_MAP[ncoord]


def write_cell(field: list[list[str]], idx: tuple[int, int]) -> bool:
    ridx, cidx = idx
    if field[ridx][cidx] == " ":
        field[ridx][cidx] = "X"
        return True
    return False
