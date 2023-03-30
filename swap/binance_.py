from binance.spot import Spot as Client
from api import interface
from api.controllers import tokens

client = Client()


pairs = {
    token['symbol'] + token['pair']: token['address']
    for token in tokens.get() if token['pair'] is not None
}

def get_prices():
    return {
        pairs[price['symbol']]: {
            'buy': 1 / float(price['price']),
            'sell': float(price['price'])
        }
        for price in client.ticker_price() if price['symbol'] in pairs
    }