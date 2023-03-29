import subprocess
from api import app
from config import HOST, PORT


swaps = {
    'uniswap': {
        2 : [3000],
        3 : [3000, 10000],
    },
    'sushiswap': {
        2 : [3000],
    }
}


def start(*args):
    print(*args)
    return subprocess.Popen(['python3.10', 'swap/track.py', *args])

if __name__ == '__main__':
    # processing = [ 
    # start(swap, str(fee), str(version))
    #     for swap, version in swaps.items()
    #         for version, fees in version.items()
    #             for fee in fees
    # ]            

    app.run(HOST, PORT)


