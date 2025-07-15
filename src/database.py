from commands import CREATE_TABLES_COMMANDS
from sqlite3 import Connection, Cursor, connect
from typing import Generator


class BaseDatabase:
    def __init__(self, path: str) -> None:
        self.path = path

    def session_maker(self) -> Generator[tuple[Connection, Cursor]]:
        with connect(self.path) as session:
            yield session, session.cursor()
