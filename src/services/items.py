from data_types import BaseItem, NullableBaseItem, Item
from dao import ItemsDAO
from utils import get_user_choice
from sqlite3 import IntegrityError

ITEM_MENU = """1. Посмотреть все товары
2. Поиск товаров по имени
3. Создать товар
4. Изменить товар
0. Выход"""
ITEM_CHOICES = {0, 1, 2, 3, 4}


def print_item(i: Item):
    print(f"{i.id} {i.title}, {i.weight} кг.")


def print_list_items(items: list[Item]):
    print()
    for item in items:
        print_item(item)
    print()


def get_item_data_from_user() -> BaseItem:
    title = input("Имя товара: ")
    weight = int(input("Вес товара: "))
    return BaseItem(title, weight)


def get_item_data_from_user_to_update(item: Item) -> NullableBaseItem:
    title = input(f"Имя товара [{item.title}]: ")
    weight = input(f"Вес товара [{item.weight}]: ")
    if not weight.isnumeric():
        raise TypeError
    return NullableBaseItem(item.id, title, int(weight))


def item_menu(items_dao: ItemsDAO):
    while True:
        print(ITEM_MENU)
        user_input = get_user_choice(ITEM_CHOICES)
        match user_input:
            case 0:
                break
            case 1:
                items = items_dao.get_all_items()
                print_list_items(items)
            case 2:
                title = input("Введите имя: ")
                items = items_dao.get_items_by_title(title)
                print_list_items(items)
            case 3:
                item = get_item_data_from_user()
                try:
                    result = items_dao.create_item(item)
                except IntegrityError:
                    print("Название товара уже занято!")
                else:
                    print_item(result)
            case 4:
                try:
                    id_ = int(input("Введите id товара для его изменения: "))
                    item = items_dao.get_item_by_id(id_)
                except ValueError:
                    print("Вы ввели невалидный id")
                    continue
                except TypeError:
                    print("Товар с этим id не обнаружен")
                    continue
                try:
                    item_to_update = get_item_data_from_user_to_update(item)
                    updated_item = items_dao.update_item(item_to_update)
                except TypeError:
                    print("Ошибка преобразования значения")
                except IntegrityError:
                    print("Имя занято!")
                else:
                    print_item(updated_item)
