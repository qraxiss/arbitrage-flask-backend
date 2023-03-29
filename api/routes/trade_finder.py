from flask_restful import Resource

from api.routes.meta.expection import ExceptionMeta
from api.controllers.trade_finder import get


class Trades(Resource, metaclass=ExceptionMeta):

    def get(self):
        return get()