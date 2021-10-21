import requests
from pprint import pprint

rates = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
# pprint(rates)

current_usd_bitcoin_rate = rates['bpi']['USD']['rate_float']

user_bitcoin = float(input('How much money bitcoin do you want to turn into dollars? '))

user_dollars = user_bitcoin*current_usd_bitcoin_rate

print(f'You would end up with ${user_dollars:.2f}')
