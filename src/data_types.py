from dataclasses import dataclass


@dataclass
class BaseItem:
    title: str
    weight: int


@dataclass
class NullableBaseItem:
    id: int
    title: str | None
    weight: int | None


@dataclass
class Item(BaseItem):
    id: int
