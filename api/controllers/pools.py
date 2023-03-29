from api.database.schemas.pools import pools as collection


def get(swap=None, fee=None, version=None, t1=None, *args, **kwargs):
    if None in [swap, fee, version, t1]:
        return list(collection.find({}, {"_id": 0}))
    
    return collection.find_one({'swap': swap, 'fee': fee,
                                'version': version, 't1': t1},
                               {"_id": 0})


def update(swap, fee, version, t1, side, price, *args, **kwargs):
    return collection.update_one({'swap': swap, 'fee': fee,
                                  'version': version, 't1': t1},
                                 {"$set": {f'{side}': price}})


def insert(*args, **kwargs):
    res = collection.insert_one(kwargs)
    return res 


{
    "swap": "uniswap",
    "fee": 3000,
    "version": 3,
    "buy": 31,
    "sell": 0.3,
    "t1": "sfsfgd",
    "t0": "432"
}

{
    "address": "fasdf",
    "decimals": 12,
    "pair": "asdfasd",
    "track": True,
    "symbol": "hihiha",
    "name": "fhşsgds"
}
