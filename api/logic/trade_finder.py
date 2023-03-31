from api import interface

from itertools import permutations

def find_profitable_trade(prices: dict, address:str)-> dict:
    trades = []
    perms = permutations(prices.items(), 2) # get all possible combinations of buy and sell
    for (buy_exchange, buy_prices),(sell_exchange, sell_prices) in perms:
        buy = buy_prices['buy']
        sell = sell_prices['sell']

        match buy, sell:
            case (0 | None), _:
                continue
            case _ ,(0 | None):
                continue

        profit = ((buy * sell) -1) * 100 # calculate profit percentage

        trades.append({
            'buy': buy_exchange,
            'sell': sell_exchange,
            # 'buy_qty': buy,
            # 'sell_price_per_qty': sell, # 
            'profit_percentage': profit,
            'address': address
        })
    return trades

def get():
    
    prices = interface.get_best_prices() 
    binance = interface.get_binance_prices()
    prices = dict(prices)
    for address, price in binance.items():
        try:
            prices[address]['binance'] = price
        except KeyError:
            continue


    return [
        trade
            for addr, data in prices.items()
                for trade in find_profitable_trade(data, addr)
    ]