import sys
import os

if __name__ == '__main__':
    # path change to main folder
    path = os.getcwd()
    sys.path.append(path)


    from swap.pool import Pool
    script_name = sys.argv[0]

    kwargs = {
        'swap': sys.argv[1],
        'fee': int(sys.argv[2]),
        'version': int(sys.argv[3])
    }

    Pool.start_all(**kwargs)