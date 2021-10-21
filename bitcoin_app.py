import requests
from pprint import pprint

# from test_bitcoin import BitCoinError

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# pprint(rates)
def main():
    bitcoins = get_bitcoins()
    try:
        dollars = convert_dollars_to_bitcoin(bitcoins, url)
        show(bitcoins, dollars)
    except BitCoinError as e:
        print(f'Error converting. Reason: {e}')


# def get_dollars():

#     """ Get a positive number from the user """
#     while True:
#         try:
#             dollars = float(input('Enter dollars: '))
#             if dollars >= 0:
#                 return dollars
#             else:
#                 print('Enter a positive number')
#         except ValueError:
#             print('Enter a number')

def convert_dollars_to_bitcoin(dollars, url):
    res = get_result_from_api(url)
    rate = get_rates(res)
    bitcoin = convert(dollars, rate)
    return bitcoin

def get_result_from_api(url):
    try:
        res = requests.get(url)
        res.raise_for_status() # raise exception if res is not 200+
        return res.json()
    except Exception as e:
        raise BitCoinError('Error proccesing response from api') from e

def get_bitcoins():
    try:
        user_bitcoin = float(input('How much money bitcoin do you want to turn into dollars? '))
        if user_bitcoin >= 0:
            return user_bitcoin
        else:
            print('Enter a positive bitcoin amount')
    except ValueError:
        print('Enter a number')

def get_rates(res):
    try:
        current_usd_bitcoin_rate = res['bpi']['USD']['rate_float']
        return current_usd_bitcoin_rate
    except Exception as e:
        raise BitCoinError('Error proccesing response from api') from e

def convert(dollars, rate):
    return dollars * rate

def show(bitcoin, dollars):
    print(f'Today, {bitcoin:.2f} is equal to ${dollars:.2f}')

class BitCoinError(Exception):
    pass

if __name__ == '__main__':
    main()

