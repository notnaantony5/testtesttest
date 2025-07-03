from dataclasses import dataclass
import json
from typing import Any


@dataclass
class UserData:
    username: str
    fullname: str
    rating: int


class UserService:
    def __init__(self, path="users.json"):
        self.path = path

    def _get_dicts_user_data(self) -> list[dict[str, Any]]:
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_users_data(self) -> list[UserData]:
        user_dicts = self._get_dicts_user_data()
        result = []
        for user_data in user_dicts:
            result.append(UserData(**user_data))
        return result

    def get_by_username(self, username: str) -> UserData | None:
        user_dicts = self._get_dicts_user_data()
        for user_dict in user_dicts:
            if user_dict.get("username") == username:
                return UserData(**user_dict)

    def add_user_data(self, user_data: UserData) -> None:
        user_dicts = self._get_dicts_user_data()
        user_dicts.append(user_data.__dict__)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(user_dicts, f, ensure_ascii=False, indent=2)


service = UserService()
print("search", service.get_by_username("sasha2"))
print(service.get_users_data())
user_data = UserData("sasha2", "впвыа", 13)
# service.add_user_data(user_data)
