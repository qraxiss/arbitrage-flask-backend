from api.routes import Tokens, Pools, BestPrices, Trades, Binance

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Trades, '/trades')
api.add_resource(BestPrices, '/best_prices')
api.add_resource(Tokens, '/tokens')
api.add_resource(Pools, '/pools')
api.add_resource(Binance, '/binance')
