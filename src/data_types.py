from dataclasses import dataclass


@dataclass
class BaseItem:
    title: str
    weight: int


@dataclass
class Item(BaseItem):
    id: int
