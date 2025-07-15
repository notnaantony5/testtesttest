from dao import TablesDAO
from dao import ItemsDAO
from print_item import print_list_items
from settings import DB_PATH

MENU = """1. Показать все товары
2. Найти товары по ключевому слову
0. Выход"""
MENU_CHOICES = {0, 1, 2}


def get_user_choice() -> int:
    while True:
        try:
            user_input = int(input().strip())
            if user_input not in MENU_CHOICES:
                raise ValueError
        except ValueError:
            print("Это не пункт меню! Попробуйте еще раз.")
        else:
            return user_input


def main():
    print("Привет! Это программа для помощи учета товара на складе")
    tables_dao = TablesDAO(DB_PATH)
    items_dao = ItemsDAO(DB_PATH)
    tables_dao.create_tables()
    while True:
        print(MENU)
        user_input = get_user_choice()
        if user_input == 0:
            break
        if user_input == 1:
            items = items_dao.get_all_items()
            print_list_items(items)
        if user_input == 2:
            title = input("Введите название: ")
            items = items_dao.get_items_by_title(title)
            print_list_items(items)
    print("Завершение работы программы...")


if __name__ == "__main__":
    main()
