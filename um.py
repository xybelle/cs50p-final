import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if ums := re.findall(r"\bum\b", s, re.IGNORECASE):
        return len(ums)
    else:
        return 0


if __name__ == "__main__":
    main()
