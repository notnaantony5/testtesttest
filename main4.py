numbers = [1, 2, 3, 4]


def step(number: int) -> int:
    return number**2


def is_even(number: int) -> int:
    return not number % 2


for i in map(step, filter(is_even, numbers)):
    print(i)
