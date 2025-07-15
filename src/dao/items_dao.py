from data_types import Item
from database import BaseDatabase
from commands import SELECT_ALL_ITEMS, SELECT_ITEMS_BY_TITLE


class ItemsDAO(BaseDatabase):
    def get_all_items(self) -> list[Item]:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(SELECT_ALL_ITEMS)
        result = cursor.fetchall()
        return [Item(*args) for args in result]

    def get_items_by_title(self, title: str) -> list[Item]:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(SELECT_ITEMS_BY_TITLE, (f"%{title}%",))
        result = cursor.fetchall()
        return [Item(*args) for args in result]
