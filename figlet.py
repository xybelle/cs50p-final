import random
import sys

from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) == 1:
        print_message()
    elif len(sys.argv) == 2:
        sys.exit("Expected font name")
    elif len(sys.argv) == 3:
        if sys.argv[1] != '--font' and sys.argv[1] != '-f':
            sys.exit("Expected '--font' or '-f'")
        print_message(sys.argv[2])


def print_message(font=None):
    if font is None:
        font = random.choice(fonts)
    elif font not in fonts:
        sys.exit("Invalid font name")
    figlet.setFont(font=font)
    msg = input("Input: ")
    print("Output: ")
    print(figlet.renderText(msg))


main()
