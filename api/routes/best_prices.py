from flask_restful import Resource

from api.routes.meta.expection import ExceptionMeta
from api.controllers.best_prices import get


class BestPrices(Resource, metaclass=ExceptionMeta):

    def get(self):
        return get()