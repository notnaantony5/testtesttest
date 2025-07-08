from typing import Callable
from datetime import datetime


def get_time(*, echo: bool) -> Callable:
    def outer_wrapper(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            func(*args, **kwargs)
            end_time = datetime.now()
            result = (end_time - start_time).total_seconds()
            if echo:
                print(result)

        return wrapper

    return outer_wrapper


@get_time(echo=True)
def test(end: int) -> None:
    print(end)
    for _ in list(range(end)):
        pass


print("start")
test(end=40_000_000)
print("end")
