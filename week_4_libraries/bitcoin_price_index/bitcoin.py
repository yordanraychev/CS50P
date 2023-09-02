import requests
from sys import argv, exit

if len(argv) != 2:
    exit("Missing command-line argument")
try:
    bitcoin_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]
    bitcoins = float(argv[1])
except (requests.RequestException, KeyError, ValueError):
    exit("Command-line argument is not a number")

print(f"${bitcoins * bitcoin_price:,.4f}")
