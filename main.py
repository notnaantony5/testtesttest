from datetime import datetime

numbers = list(range(50_000_000))


def func(numbers: list[int]) -> dict[int, int]:
    step_numbers = {}
    for number in numbers:
        if number % 2:
            step_numbers[number] = number**2
    return step_numbers


def func2(numbers: list[int]):
    return (number for number in numbers if number % 2)


input(":")
start_time = datetime.now()
for num in func(numbers):
    num
print(datetime.now() - start_time)
input(":")
start_time = datetime.now()
for num in func2(numbers):
    num
print(datetime.now() - start_time)
input(":")
