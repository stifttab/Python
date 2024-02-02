import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        bitcoin_data = response.json()
        return bitcoin_data['bpi']['USD']['rate_float']
    except requests.RequestException as e:
        print(f"Error: Unable to fetch Bitcoin price - {e}")
        sys.exit(1)

def main():
    if len(sys.argv) == 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    formatted_total_cost = num_bitcoins * bitcoin_price

    print(f"${formatted_total_cost:,.4f}")
main()
