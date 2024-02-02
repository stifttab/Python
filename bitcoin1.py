import sys
import requests

def main():
    if len(sys.argv) == 2:
        try:
            bitcoin_price = float(sys.argv[1])
        except:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response = btc.json()
        bitcoin = response ['bpi']['USD']['rate_float']
        total_amount = bitcoin * bitcoin_price 
        print(f"${total_amount:,.4f}")
    except requests.RequestException:
            print("RequestException")
            sys.exit(1)
if __name__ == "__main__":
    main()    