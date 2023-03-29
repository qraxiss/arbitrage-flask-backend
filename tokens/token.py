from web3 import Web3


class Token:
    def __init__(self, address, name, symbol, decimals, pair, track) -> None:
        self.address = address
        self.checksum_address = Web3.toChecksumAddress(address)
        self.name = name
        self.symbol = symbol
        self.decimals = decimals
        self.pair = pair
        self.track = track

        self.qty = 10 ** self.decimals
        self.symbol_pair = self.symbol + self.pair

