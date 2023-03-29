from api.routes import Tokens, Pools

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Tokens, '/tokens')
api.add_resource(Pools, '/pools')
