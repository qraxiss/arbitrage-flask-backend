from config import HOST, PORT, PROTOCOL

from requests import get, patch, post

class Interface:
    URL = f'{PROTOCOL}://{HOST}:{PORT}'

    def get_token(self, address=None):
        return get(f'{self.URL}/tokens', json={
            "address": address
        }).json()
    
    def set_track(self, address,track):
        return patch(f'{self.URL}/tokens', json={
            "address": address,
            "track": track
        }).json()
    
    def add_token(self, token):
        return post(f'{self.URL}/tokens', json=token).json()

    
    def get_pool(self, swap=None, fee=None, version=None, t1=None):
        return get(f'{self.URL}/pools', json={
            "swap": swap,
            "fee": fee,
            "version": version,
            "t1": t1,
            }
        ).json()
    
    def update_price(self, swap, fee, version, t1, side, price):
        return patch(f'{self.URL}/pools', json={
            "swap": swap,
            "fee": fee,
            "version": version,
            "t1": t1,
            "side": side,
            "price": price
        }).json()
    
    def add_pool(self, pool):
        return post(f'{self.URL}/pools', json=pool).json()