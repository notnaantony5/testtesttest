from field_utils import generate_field
from printing import print_field, print_hello


def main():
    print_hello()
    field = generate_field()
    print_field(field)


if __name__ == "__main__":
    main()
