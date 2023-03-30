from api import interface

from itertools import permutations

def find_profitable_trade(prices: dict, address:str)-> dict:
    trades = []
    for (buy_exchange, buy_prices),(sell_exchange, sell_prices) in permutations(prices.items(), 2):
        buy = buy_prices['buy']
        sell = sell_prices['sell']

        match buy, sell:
            case (0 | None), _:
                continue
            case _ ,(0 | None):
                continue

        profit = ((buy * sell) -1) * 100

        trades.append({
            'buy_exchange': buy_exchange,
            'sell_exchange': sell_exchange,
            'buy_price': buy,
            'sell_price': 1/sell,
            'profit_percentage': profit,
            'address': address
        })
    return trades

def get():
    swaps =  interface.get_best_prices()
    return [
        trade
            for addr, data in swaps.items()
                for trade in find_profitable_trade(data, addr)
    ]