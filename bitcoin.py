import json
import requests
import sys

# Ensure user specify as a CL argument the number of BTC
if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py n")

# Ensure user enters a number in CL
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("n is not a number")

# Error handling for request.get() call
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Error: Unable to retrieve data from CoinDesk API.")

res = response.json()

# Error handling if structure of the JSON response changes
try:
    price = res["bpi"]["USD"]["rate"].replace(",", "")
except KeyError:
    sys.exit("Error: Unexpected structure in JSON response. Unable to find expected keys.")

# Get current cost
current_cost = n * float(price)

print(f"${current_cost:,.4f}")
