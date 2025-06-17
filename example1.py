from typing import Callable


GREETING = "Привет, %s!"


def func() -> Callable:
    text = GREETING

    def hello(name: str) -> str:
        return text % name

    return hello


hello1 = func()
GREETING = "ПРИВЕТИЩЕ, %s!"
hello2 = func()
print(hello1("TEST"))
print(hello2("TEST"))
