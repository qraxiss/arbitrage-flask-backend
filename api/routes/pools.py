from flask_restful import Resource
from api.routes.meta.metaclass import MetaClass
from flask import request


class Pools(Resource, metaclass=MetaClass):
    import api.controllers.pools as controllers
    def get(self):
        ...

    def patch(self):
        self.controllers.update(**request.json)

    def post(self):
        self.controllers.insert(**request.json)
