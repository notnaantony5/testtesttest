from data_types import Item


def print_item(i: Item):
    print(f"{i.id} {i.title}, {i.weight} кг.")


def print_list_items(items: list[Item]):
    print()
    for item in items:
        print_item(item)
    print()
