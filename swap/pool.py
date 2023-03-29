from uniswap import Uniswap
from random import choice

# exceptions
from requests.exceptions import ConnectionError as TooManyRequests # thread limit
from web3.exceptions import ContractLogicError

# local imports
from api import interface
from helpers import thread, set_timeout
from tokens.token import Token
from swap.forks import Forks



class Pool:
    

    exchanges = {
        'sushiswap': {
            2: Forks.create_swaps('sushiswap', 2)
        },
        'uniswap': {
            2: Forks.create_swaps('uniswap', 2),
            3: Forks.create_swaps('uniswap', 3)
        },
    }

    @classmethod
    def start_all(cls, swap, version, fee):
        tokens = interface.get_token()
        for token in tokens:
            t1 = Token(**token)
            if t1.track:
                token = [token for token in tokens if token['symbol'] == t1.pair][0]
                t0 = Token(**token)
                pool = cls(swap, version, fee, t0=t0, t1=t1)
                pool.start()
    

    def __init__(self, swap: str, version: int, fee: int, t0: Token, t1: Token) -> None:
        self.swap = swap
        self.version = version
        self.fee = fee
        self.t0 = t0
        self.t1 = t1
        self.buy = -1
        self.sell = -1

        # if pool not exist in collection
        pool = self.interface.get_pool(self.swap, self.fee, self.version, self.t1.address)
        if pool is None:
            self.interface.add_pool({
                "swap": self.swap,
                "fee": self.fee,
                "version": self.version,
                "t0": self.t0.address,
                "t1": self.t1.address,
                "buy": self.buy,
                "sell": self.sell
            })
    
    @property
    def fork(self) -> Uniswap:
        return choice(self.exchanges[self.swap][self.version])

    def get_price(self, side) -> float:
        address = [self.t0.checksum_adrress, self.t1.checksum_adrress]
        address = address if side == 'buy' else address[::-1]

        # version 3 not support route        
        route = None if self.version == 3 else address

        price_func = getattr(self.fork, Forks.sides[side])
        price = price_func(*address, self.t0.qty,fee=self.fee, route=route) / self.t1.qty

        return price if side == 'buy' else 1/price

    def start(self):
        self.track('buy')
        self.track('sell')

    @thread
    def track(self, side):
        # I use set_timeout instead of while True: because 
        # exception handling and time controls are easier on recursion

        # And recursion depth is not a problem because the new
        # function is not called before the function is closed.

        try:
            price = self.get_price(side)
            set_timeout(lambda: self.track(side), 12)
            self.update(price, side)

        except ContractLogicError as e:
            self.error_log(e, side)
            self.update(-1, side)
            # 10 minutes + random 0-5 minutes
            # set_timeout(lambda: self.track(side), 10 * 60 + choice(range(300))) 

        except TooManyRequests as e:
            self.error_log(e, side)

            # sleep time is random between 0 and 65 seconds to avoid too many requests
            sleep_sec = choice(range(65)) 
            set_timeout(lambda: self.track(side), sleep_sec) 
        
        except Exception as e:
            # print(f'{self.version} {self.swap}, {self.fee}, {self.t1.symbol_pair}, {(e)}')
            self.error_log(e, side)
            set_timeout(lambda: self.track(side), 60)

    def update(self, price: float, side) -> None:
        def is_update() -> bool:
            return not getattr(self, side) == price

        update = is_update()
        if update:
            self.log(update, getattr(self, side), price, side)

            # update price in memory
            setattr(self, side, price)

            # update price in db
            self.interface.update_price(self.swap, self.fee, 
                                        self.version, self.t1.address, 
                                        side, price) 
            
            

    def error_log(self, e: Exception, side:str) -> None:
        print(f'{self.version} {self.swap}, {self.fee}, {side}, {self.t1.symbol_pair}, {type(e)}')

    def log(self, update: bool, old: float, new: float, side: str) -> None:
        sign = '->' if update else '=='
        print(f'{self.version} {self.swap}, {self.fee}, {side}, {self.t1.symbol_pair} {old} {sign} {new}')