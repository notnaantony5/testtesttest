from dao.movements_dao import MovementsDAO
from data_types import BaseMovement, Movement, MovementType
from utils import get_user_choice
from datetime import datetime

MOVEMENTS_MENU = """1. Перемещения товара
2. Создать перемещение товара
0. Выход"""
MOVEMENTS_CHOICES = {0, 1, 2}


def print_movement(m: Movement) -> None:
    print(m)


def print_list_movements(movements: list[Movement]) -> None:
    for m in movements:
        print_movement(m)


def get_movement_data() -> BaseMovement:
    item_id = int(input("Айди товара: "))
    created_at = datetime.now()
    count = int(input("Количество: "))
    if (type_number := int(input("Тип: 1 - приход, 2 - уход\n: "))) not in {1, 2}:
        raise ValueError
    type_ = MovementType.income if type_number == 1 else MovementType.outcome
    return BaseMovement(item_id, created_at, count, type_)


def movements_menu(movements_dao: MovementsDAO) -> None:
    while True:
        print(MOVEMENTS_MENU)
        user_input = get_user_choice(MOVEMENTS_CHOICES)
        match user_input:
            case 0:
                break
            case 1:
                movements = movements_dao.get_all_movements()
                print_list_movements(movements)
            case 2:
                base_movement = get_movement_data()
                movement = movements_dao.create_movement(base_movement)
                print_movement(movement)
