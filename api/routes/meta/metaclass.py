from api.routes.meta.expection import ExceptionMeta
from flask import request


def return_item(func, controllers):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return controllers.get(**request.json)
    return wrapper


class MetaClass(ExceptionMeta):
    def __new__(cls, name, bases, attrs, ):
        cls.apply_decorator(attrs, return_item, attrs['controllers'])
        return super().__new__(cls, name, bases, attrs)