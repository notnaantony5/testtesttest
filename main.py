from dataclasses import dataclass


class Service:
    endpoint = "test"

    @classmethod
    def call(cls):
        print(cls.endpoint)


# Service.call()


@dataclass
class UserData:
    login: str
    age: int


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

    @classmethod
    def from_userdata(cls, user_data: UserData):
        return cls(user_data.login, user_data.age)


user_data = UserData("test", 22)
user = User.from_userdata(user_data)
print(user.age)


class UserService:
    atrib = 22

    @staticmethod
    def func():
        return


class PostService:
    @staticmethod
    def func(text: str):
        return text


PostService.func("text")
UserService.func()
