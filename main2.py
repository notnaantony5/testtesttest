from pickletools import string1


class User:
    def __init__(self, username: str):
        self.username = username
        self._is_muted = False
        self.role = "user"

    def set_muted(self):
        self._is_muted = True

    def get_role_name(self):
        return f"{self.role} {self.username}"

    def write(self, message: str):
        if not self._is_muted:
            print(f"{self.get_role_name()}: {message}")
        else:
            print(f"{self.get_role_name()} молчит")


class Admin(User):
    def __init__(self, username: str, role="admin"):
        super().__init__(username)
        self.role = role

    def set_muted(self):
        pass

    def mute(self, user: User):
        user.set_muted()
        print(f"Администратор {self.username} заглушил {user.username}")


user1 = User("sasha")
user1.write("Првиет всем!")
admin1 = Admin("admin", "best_admin")
admin1.write("Всем привет!")
user1.write("********")
admin1.mute(user1)
user1.write("Я пошутил!")
# class Animal:
# class Cat(Animal):
# class Wolf(Animal):
# class Dog(Wolf):


# Класс животное - имеет цвет
# Класс волк имеет цвет, имеет возможность говорить say() -> "воет"
# Класс собака имеет цвет, имеет возможность говорить say() -> "гав" и имеет имя (атрибут name)
class Animal:
    def __init__(self, color: str) -> None:
        self.color = color


class Cat(Animal):
    def say(self):
        print("Мяу")


class Wolf(Animal):
    def say(self):
        print("воет")


class Dog(Wolf):
    def __init__(self, color: str, name: str) -> None:
        super().__init__(color)
        self.name = name

    def say(self):
        print("гав")
