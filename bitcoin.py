import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py n")
elif not sys.argv[1].isdigit():
    sys.exit("n is not an integer")

n = float(sys.argv[1])

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()

res = response.json()
price = res["bpi"]["USD"]["rate"].replace(",", "")
current_cost = n * float(price)

print(f"${current_cost:,.4f}")
