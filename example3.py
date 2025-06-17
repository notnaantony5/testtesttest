def summ(*numbers: int):
    print(numbers)
    result = 0
    for number in numbers:
        result += number
    return result


col = [1, 7, 12]
col2 = [20, 30]

print(summ(*col, *col2))


def step(number: int, s: int) -> int:
    return number**s


data = (6, 2)
print(step(*data))

name = ("Иванов", "Иван", "Иванович")
print(*name)


def j(*strings: str, sep=" ") -> str:
    print(sep)
    print(strings)
    result = ""
    for string in strings:
        result += string + sep
    return result


print(j("|", "ba", "sad"))


def func(a, *args, s, b=2, **kwargs):
    print("a", a)
    print("args", args)
    print("s", s)
    print("b", b)
    print("kwargs", kwargs)


func(2, "s", 7, 1, g=6, v=8, s=9)
d = dict(g=2, s=7)
print("d", d)
