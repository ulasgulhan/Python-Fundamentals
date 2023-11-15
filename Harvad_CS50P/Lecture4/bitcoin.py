import requests
import sys


if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print('Commend-line argument is not a number')
        sys.exit()
else:
    print('Missing commend-line argument')
    sys.exit()
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r = response.json()
    amount = float(r['bpi']['USD']['rate_float']) * value
    print(f'{amount:,.4f}')
except requests.RequestException:
    print('RequestException')
    sys.exit()