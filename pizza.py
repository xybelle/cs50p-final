import csv
import sys

from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")


table = []

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for line in reader:
            table.append(line)
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")

