from sqlite3 import IntegrityError
from dao import TablesDAO
from dao import ItemsDAO
from data_types import BaseItem
from print_item import print_list_items, print_item
from settings import DB_PATH

MENU = """1. Работа с товарами
0. Выход"""
MENU_CHOICES = {0, 1}

ITEM_MENU = """1. Посмотреть все товары
2. Поиск товаров по имени
3. Создать товар
0. Выход"""
ITEM_CHOICES = {0, 1, 2, 3}


def get_item_data_from_user() -> BaseItem:
    title = input("Имя товара: ")
    weight = int(input("Вес товара: "))
    return BaseItem(title, weight)


def get_user_choice(choices: set[int]) -> int:
    while True:
        try:
            user_input = int(input().strip())
            if user_input not in choices:
                raise ValueError
        except ValueError:
            print("Это не пункт меню! Попробуйте еще раз.")
        else:
            return user_input


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


def main():
    print("Привет! Это программа для помощи учета товара на складе")
    tables_dao = TablesDAO(DB_PATH)
    items_dao = ItemsDAO(DB_PATH)
    tables_dao.create_tables()
    while True:
        print(MENU)
        user_input = get_user_choice(MENU_CHOICES)
        if user_input == 0:
            break
        if user_input == 1:
            item_menu(items_dao)

    print("Завершение работы программы...")


if __name__ == "__main__":
    main()
