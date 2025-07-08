from typing import Callable


def print_args(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        return result

    return wrapper


@print_args
def test(*args, **kwargs):
    pass


test(1212, 343, a=543, ns="fdsf")
