from api import interface

from itertools import permutations

def find_profitable_trade(prices: dict)-> dict:
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
        })
    return trades

def get():
    prices =  interface.get_best_prices()
    return {
        addr: find_profitable_trade(data)
        for addr, data in prices.items()
    }