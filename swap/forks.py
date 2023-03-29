from uniswap import Uniswap
from web3 import Web3, HTTPProvider
from concurrent.futures import ThreadPoolExecutor

from config import providers

class Forks:
    sides = {
        'buy': 'get_price_input',
        'sell': 'get_price_output'
    }

    def sushiswap(provider, version) -> Uniswap:
        sushi_factory = '0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac'
        sushi_router = '0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F'

        web3 = Web3(HTTPProvider(provider))

        return Uniswap(
            address=None, private_key=None, version=version,
            factory_contract_addr=sushi_factory,
            router_contract_addr=sushi_router,
            web3=web3
        )

    def uniswap(provider, version) -> Uniswap:
        web3 = Web3(HTTPProvider(provider))

        return Uniswap(
            address=None, private_key=None, version=version,
            web3=web3
        )

    def create_swaps(fork, version) -> list[Uniswap]:
        with ThreadPoolExecutor(max_workers=len(providers)) as executor:

            futures = [executor.submit(
                getattr(Forks, fork),
                provider, version
            )
                for provider in providers]

        return [
            future.result() for future in futures
        ]
