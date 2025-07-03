import json
from dataclasses import dataclass


@dataclass
class UserData:
    username: str
    fullname: str
    rating: int


with open("users.json", "r", encoding="utf-8") as f:
    data: list[dict] = json.load(f)
for row in data:
    try:
        while True:
            UserData(**row)
            break
    except TypeError as e:
        if str(e).split("'")[1] == "rating":
            row["rating"] = 0

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
