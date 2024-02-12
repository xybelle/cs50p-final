import random
import sys

from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.srgv) == 2:
        sys.exit("Expected font name")
    elif len(sys.argv) == 1:
        print_message()
    elif len(sys.argv) == 3:
        if sys.argv[1] != '--font' and sys.argv[1] != '-f':
            sys.exit("Expected '--font' or '-f'")
        elif sys.argv[2] not in fonts:
            sys.exit("Invalid font name")
        print_message(sys.argv[2])


def print_message(font=None):
    msg = input("Input: ")
    if font is None:
        font = random.choice(fonts)
    figlet.setFont(font=font)
    print("Output: ")
    print(figlet.renderText(msg))


main()
