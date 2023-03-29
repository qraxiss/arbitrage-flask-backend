import api.controllers.pools as controllers_pools

from config import FEE

import pandas as pd

def get():
    pools = controllers_pools.get()

    df = pd.DataFrame([pool for pool in pools 
                        if pool['buy'] != -1 or 
                           pool['sell'] != -1]
                        )

    df[df[['buy','sell']] < 0] = float('NaN')

    df['actual_buy'] = df['buy'] - (df['buy'] * (df['fee']/FEE))
    df['actual_sell'] = df['sell'] + (df['sell'] * (df['fee']/FEE))
    gb = df.groupby(['t1', 'swap'], group_keys=True)[['actual_buy', 'actual_sell', 'buy', 'sell']]



    df = pd.DataFrame([gb.max()['buy'], gb.min()['sell']])
    df[df.isna()] = None
    return df.to_dict()