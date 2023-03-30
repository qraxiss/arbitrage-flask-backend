from api.controllers.binance_ import get_prices

from flask_restful import Resource
from api.routes.meta.metaclass import ExceptionMeta


class Binance(Resource, metaclass=ExceptionMeta):
    def get(self):
        return get_prices()