from functools import wraps
import inspect

def generate_constructors(cls):
    attributes = [name for name, _ in cls.__annotations__.items() if name != 'return']

    @wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        return instance

    def generate_constructor(*constructor_args):
        @wraps(cls)
        def constructor_wrapper(*args, **kwargs):
            instance = cls(*args, **kwargs)
            return instance

        return constructor_wrapper

    for i in range(0, len(attributes) + 1):
        constructor_args = attributes[:i]
        constructor_name = '__init__' + '_'.join(constructor_args)
        constructor = generate_constructor(*constructor_args)
        setattr(wrapper, constructor_name, constructor)

    return wrapper
