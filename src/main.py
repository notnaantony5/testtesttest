from bot_utils import bot_turn
from field_utils import generate_field, write_cell, tranform_coord_to_index
from printing import print_field, print_hello
from user_input import get_user_coordinates_input


def main():
    print_hello()
    field = generate_field()
    while True:
        print_field(field)
        while True:
            coord = get_user_coordinates_input()
            idx = tranform_coord_to_index(coord)
            if write_cell(field, idx):
                break
            print("Ячейка занята")
        bot_turn(field)


if __name__ == "__main__":
    main()
