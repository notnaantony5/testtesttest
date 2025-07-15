from data_types import Item
from database import BaseDatabase
from commands import SELECT_ALL_ITEMS


class ItemsDAO(BaseDatabase):
    def get_all_items(self) -> list[Item]:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(
            SELECT_ALL_ITEMS, ("Мяч",)
        )  # параметры убрать после реализации своего метода
        result = cursor.fetchall()
        return [Item(*args) for args in result]
