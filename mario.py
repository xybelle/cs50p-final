from cs50 import get_int


def main():
    while True:
        height = get_int("Height: ")
        if 0 < height <= 8:
            break
    draw(height)


def draw(h):
    for i in range(h):
        for j in range(h - (i+1)):
            print(" ", end="")
        for k in range(i + 1):
            print("#", end="")
        print()


main()
