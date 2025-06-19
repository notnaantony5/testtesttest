lenght = int(input(": "))
for i in range(lenght):
    print(" " * (lenght - i - 1) + "0", end="")
    if i:
        print(" " * (i * 2 - 1) + "0")
    else:
        print()
for i in range(lenght - 2, -1, -1):
    print(" " * (lenght - i - 1) + "0", end="")
    if i:
        print(" " * (i * 2 - 1) + "0")
    else:
        print()
