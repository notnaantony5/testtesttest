from dataclasses import dataclass
import json


@dataclass
class UserData:
    username: str
    fullname: str
    rating: int


class UserService:
    def __init__(self, path="users.json"):
        self.path = path

    def get_users_data(self):
        result = []
        with open(self.path, "r", encoding="utf-8") as f:
            for user_data in json.load(f):
                result.append(UserData(**user_data))
        return result


service = UserService()
print(service.get_users_data())
