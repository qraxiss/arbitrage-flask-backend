from flask_restful import Resource
from flask import request
from api.routes.meta.metaclass import MetaClass


class Tokens(Resource, metaclass=MetaClass):
    import api.controllers.tokens as controllers
    def get(self):
        ...

    def patch(self):
        self.controllers.update(**request.json)

    def post(self):
        self.controllers.insert(**request.json)
