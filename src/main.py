from bot_utils import bot_turn
from field_utils import generate_field
from printing import print_field, print_hello
from user_input import user_turn


def main():
    print_hello()
    field = generate_field()
    while True:
        print_field(field)
        user_turn(field)
        bot_turn(field)


if __name__ == "__main__":
    main()
