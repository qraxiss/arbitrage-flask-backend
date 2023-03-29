from config import HOST, PORT, PROTOCOL

from requests import get, patch, post

URL = f'{PROTOCOL}://{HOST}:{PORT}'


def get_token(address=None):
    return get(f'{URL}/tokens', json={
        "address": address
    }).json()


def set_token_track(address, track):
    return patch(f'{URL}/tokens', json={
        "address": address,
        "track": track
    }).json()


def add_token(token):
    return post(f'{URL}/tokens', json=token).json()


def get_pool(swap=None, fee=None, version=None, t1=None):
    return get(f'{URL}/pools', json={
        "swap": swap,
        "fee": fee,
        "version": version,
        "t1": t1,
    }
    ).json()


def update_price(swap, fee, version, t1, side, price):
    return patch(f'{URL}/pools', json={
        "swap": swap,
        "fee": fee,
        "version": version,
        "t1": t1,
        "side": side,
        "price": price
    }).json()


def update_volume(swap, fee, version, t1, volume):
    return patch(f'{URL}/pools', json={
        "swap": swap,
        "fee": fee,
        "version": version,
        "t1": t1,
        "side": "volume",
        "price": volume
    }).json()

def add_pool(pool):
    return post(f'{URL}/pools', json=pool).json()


def get_best_prices():
    return get(f'{URL}/best_prices').json()


def open_pair(address):
    return set_token_track(address, True)

def close_pair(address):
    return set_token_track(address, False)

def open_all_tokens():
    for token in get_token():
        open_pair(token['address'])

def close_all_tokens():
    for token in get_token():
        close_pair(token['address'])

def open_pool(swap, fee, version, t1):
    return update_volume(swap, fee, version, t1, True)

def close_pool(swap, fee, version, t1):
    return update_volume(swap, fee, version, t1, False)

def open_all_pools():
    for pool in get_pool():
        open_pool(**pool)

def close_all_pools():
    for pool in get_pool():
        close_pool(**pool)