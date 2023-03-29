from flask_restful import Resource
from flask import request
from api.routes.meta.expection import ExceptionMeta

from config import FEE

import pandas as pd

class BestPrices(Resource, metaclass=ExceptionMeta):
    import api.controllers.tokens as tokens
    import api.controllers.pools as pools

    def get(self):
        
        return 