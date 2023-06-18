def multi_constructor(cls):
    """
    A decorator that modifies the constructor of a class to take keyword arguments.
    This allows the class to be instantiated with any subset of its original arguments.

    This decorator modifies the class's __init__ method to only consider parameters
    that are included in the keyword arguments passed upon instantiation.

    Note: This will only work for arguments that have a default value or are optional,
    as it doesn't provide a way to handle missing required arguments.

    :param cls: The class whose __init__ method will be modified.
    :return: The modified class.
    """
    init = cls.__init__

    params = init.__code__.co_varnames[1: init.__code__.co_argcount]

    def new_init(self, **kwargs):
        init(self, **{k: kwargs[k] for k in params if k in kwargs})

    cls.__init__ = new_init
    return cls
