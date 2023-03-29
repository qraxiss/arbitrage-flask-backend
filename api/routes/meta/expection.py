def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error = {'error': type(e).__name__, 'description': str(e)}
            return error, 500
    return wrapper


class ExceptionMeta(type):

    def __new__(cls, name, bases, attrs):
        cls.apply_decorator(attrs, handle_exceptions)
        return type.__new__(cls, name, bases, attrs)
    
    @classmethod
    def apply_decorator(cls, attrs, decorator, *args):
        for key, value in attrs.items():
            if callable(value):
                attrs[key] = decorator(value, *args)