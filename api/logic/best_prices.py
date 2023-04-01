# local imports
from api import interface
from config import FEE

# data manipulation
from collections import defaultdict
import pandas as pd
import numpy as np



def get():
    pools = interface.get_pool()
    tokens = {
        token['address']: token 
              for token in interface.get_token()
        }

    df = pd.DataFrame([pool for pool in pools 
                        if pool['volume'] and (pool['buy'] != -1 or 
                           pool['sell'] != -1)]
                        )

    df[df[['buy','sell']] < 0] = float('NaN')

    df['actual_buy'] = df['buy'] - (df['buy'] * (df['fee']/FEE))
    df['actual_sell'] = df['sell'] + (df['sell'] * (df['fee']/FEE))
    gb = df.groupby(['t1', 'swap'], group_keys=True)[['actual_buy', 'actual_sell', 'buy', 'sell']]

    df = pd.DataFrame([gb.max()['buy'], gb.min()['sell']])
    df.replace(to_replace=[np.nan], value=[None], inplace=True)
    
    prices = defaultdict(dict)
    for address, swap in df.columns:
        if not tokens[address]['track']:
            continue

        prices[address][swap] = {**df[address][swap]}

    return prices