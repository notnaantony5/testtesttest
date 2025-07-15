from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    weight: int
