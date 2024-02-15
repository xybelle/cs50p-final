import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        count = 0
        for line in file:
            if line.startswith("#"):
                continue
            elif line.lstrip() == "":
                continue
            elif line.lstrip().startswith("#"):
                continue

            count += 1
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")

