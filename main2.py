import json


def get_user_input() -> int:
    return int(input(":"))


def multuply(num: int) -> int:
    return num * 2


def division(num: int) -> float:
    return 100 / multuply(num)


def write_to_json(num: float) -> list[float]:
    with open("file.json", "r", encoding="utf-8") as f:
        numbers = json.load(f)
    numbers.append(num)
    with open("file.json", "w", encoding="utf-8") as f:
        json.dump(numbers, f)
    return numbers


def main():
    try:
        input = division(get_user_input())
        try:
            numbers = write_to_json(input)
        except FileNotFoundError:
            with open("file.json", "w") as f:
                f.write("[]")
            numbers = write_to_json(input)
        print(numbers)
    except ValueError as e:
        print(f"Вы ввели не число {e}")
    except ZeroDivisionError:
        print("Делить на ноль нельзя")


main()
